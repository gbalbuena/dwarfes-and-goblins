// SPDX-License-Identifier: MIT
pragma solidity 0.8.9;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/interfaces/IERC2981.sol";
import "@openzeppelin/contracts/interfaces/IERC20.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@chainlink/contracts/src/v0.8/interfaces/VRFCoordinatorV2Interface.sol";
import "@chainlink/contracts/src/v0.8/interfaces/LinkTokenInterface.sol";
import "@chainlink/contracts/src/v0.8/VRFConsumerBaseV2.sol";

import {IProxyRegistry} from "./../external/opensea/IProxyRegistry.sol";

import "./CreatureFactory.sol";

contract CreatureToken is
    ERC721Enumerable,
    CreatureFactory,
    VRFConsumerBaseV2
{
    VRFCoordinatorV2Interface immutable COORDINATOR;
    LinkTokenInterface immutable LINKTOKEN;

    IProxyRegistry public immutable proxyRegistry;
    // Your subscription ID.
    uint64 immutable s_subscriptionId;

    // The gas lane to use, which specifies the maximum gas price to bump to.
    // For a list of available gas lanes on each network,
    // see https://docs.chain.link/docs/vrf-contracts/#configurations
    bytes32 immutable s_keyHash;

    // Depends on the number of requested values that you want sent to the
    // fulfillRandomWords() function. Storing each word costs about 20,000 gas,
    // so 100,000 is a safe default for this example contract. Test and adjust
    // this limit based on the network that you select, the size of the request,
    // and the processing of the callback request in the fulfillRandomWords()
    // function.
    uint32 immutable s_callbackGasLimit = 100000;

    // The default is 3, but you can set this higher.
    uint16 immutable s_requestConfirmations = 3;

    // For this example, retrieve 2 random values in one request.
    // Cannot exceed VRFCoordinatorV2.MAX_NUM_WORDS.
    uint32 immutable s_numWords = 2;

    uint256[] public s_randomWords;
    uint256 public s_requestId;
    address s_owner;

    event ReturnedRandomness(uint256[] randomWords);
    constructor(
        IProxyRegistry _openSeaProxyRegistryAddress,
        uint64 subscriptionId,
        address vrfCoordinator,
        address link,
        bytes32 keyHash
    ) ERC721("Creatures", "CREA") VRFConsumerBaseV2(vrfCoordinator) {
        proxyRegistry = _openSeaProxyRegistryAddress;
        COORDINATOR = VRFCoordinatorV2Interface(vrfCoordinator);
        LINKTOKEN = LinkTokenInterface(link);
        s_subscriptionId = subscriptionId;
        s_keyHash = keyHash;
        s_owner = msg.sender;
    }

    function publicMint(string memory _name) public {
        require(s_requestId != 0, "Please initalize randomness");

        uint256 randDna = _generateRandomDna(
            uint256(s_randomWords[0])
        );
        Race race_ = Race.Dwarf;

        creatures.push(Creature(_name, race_, randDna));
        uint256 creatureId = creatures.length - 1;
        _createCreature(_name, race_, randDna);
        _safeMint(msg.sender, creatureId);
    }

    /**
     * @notice Callback function used by VRF Coordinator
     *
     * @param requestId - id of the request
     * @param randomWords - array of random results from VRF Coordinator
     */
    function fulfillRandomWords(uint256 requestId, uint256[] memory randomWords)
        internal
        override
    {
        s_randomWords = randomWords;
        emit ReturnedRandomness(randomWords);
    }

    modifier onlyOwner() {
        require(msg.sender == s_owner);
        _;
    }

    // Assumes the subscription is funded sufficiently.
    /**
     * @notice Requests randomness
     * Assumes the subscription is funded sufficiently; "Words" refers to unit of data in Computer Science
     */
    function requestRandomWords() external onlyOwner {
        // Will revert if subscription is not set and funded.
        s_requestId = COORDINATOR.requestRandomWords(
            s_keyHash,
            s_subscriptionId,
            s_requestConfirmations,
            s_callbackGasLimit,
            s_numWords
        );
    }
}
