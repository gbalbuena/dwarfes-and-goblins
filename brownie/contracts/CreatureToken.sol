// SPDX-License-Identifier: MIT
pragma solidity 0.8.9;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/interfaces/IERC2981.sol";
import "@openzeppelin/contracts/interfaces/IERC20.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@chainlink/contracts/src/v0.8/interfaces/VRFCoordinatorV2Interface.sol";
import "@chainlink/contracts/src/v0.8/interfaces/LinkTokenInterface.sol";
import "@chainlink/contracts/src/v0.8/VRFConsumerBaseV2.sol";

import {IProxyRegistry} from "./../external/opensea/IProxyRegistry.sol";

import "./CreatureFactory.sol";

contract CreatureToken is
    Ownable,
    ReentrancyGuard,
    ERC721Enumerable,
    CreatureFactory,
    VRFConsumerBaseV2
{
    IProxyRegistry public immutable proxyRegistry;
    VRFCoordinatorV2Interface COORDINATOR;

    LinkTokenInterface LINKTOKEN;

    uint256[] public s_randomWords;
    uint256 public s_requestId;
    address s_owner;
    uint64 public s_subscriptionId;
    bytes32 keyHash =
        0xd89b2bf150e3b9e13446986e571fb9cab24b13cea0a43ea20a6049a85cc807cc;
    address vrfCoordinator = 0x6168499c0cFfCaCD319c818142124B7A15E857ab;
    uint32 callbackGasLimit = 100000;

    address link = 0x01BE23585060835E02B77ef475b0Cc51aA1e0709;

    // The default is 3, but you can set this higher.
    uint16 requestConfirmations = 3;

    // For this example, retrieve 2 random values in one request.
    // Cannot exceed VRFCoordinatorV2.MAX_NUM_WORDS.
    uint32 numWords = 2;

    constructor(IProxyRegistry _openSeaProxyRegistryAddress, uint64 subID)
        ERC721("Creatures", "CREA")
        VRFConsumerBaseV2(vrfCoordinator)
    {
        proxyRegistry = _openSeaProxyRegistryAddress;
        LINKTOKEN = LinkTokenInterface(link);
        s_subscriptionId = subID;
        s_owner = msg.sender;
    }

    function publicMint(string memory _name) public {
        require(s_requestId!= 0, "Please initalize randomness");

        uint256 randDna = _generateRandomDna(uint256(s_randomWords[s_requestId]));
        Race race_ = Race.Dwarf;

        creatures.push(Creature(_name, race_, randDna));
        uint256 creatureId = creatures.length - 1;
        _createCreature(_name, race_, randDna);
        _safeMint(msg.sender, creatureId);
    }

    function fulfillRandomWords(
        uint256, /* requestId */
        uint256[] memory randomWords
    ) internal override {
        s_randomWords = randomWords;
    }

    // Assumes the subscription is funded sufficiently.
    function requestRandomWords() external {
        // Will revert if subscription is not set and funded.
        s_requestId = COORDINATOR.requestRandomWords(
            keyHash,
            s_subscriptionId,
            requestConfirmations,
            callbackGasLimit,
            numWords
        );
    }
}
