// SPDX-License-Identifier: MIT
pragma solidity 0.8.9;

import "@openzeppelin/contracts/token/ERC721/extensions/IERC721Enumerable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC721/IERC721Receiver.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import { CreatureToken } from "./CreatureToken.sol";
import { Gold } from "./Gold.sol";

contract Mine is Ownable, ReentrancyGuard, IERC721Receiver {
    CreatureToken creatures;
    Gold gold;

    uint256 public totalPlayerStaked = 0;
    uint256 public constant DAILY_GOLD_RATE = 20 ether;
    uint256 public constant MAX_MINABLE_GOLD = 10000000 ether;

    uint256 public totalGoldEarned;
    uint256 public lastClaimTimestamp;

    event TokenStaked(address owner, uint256 tokenId, uint256 value);
    event TokenClaimed(uint256 tokenId, uint256 earned, bool unstaked);

    mapping(uint256 => Stake) public mine;

    struct Stake {
        uint16 tokenId;
        uint80 value;
        address owner;
    }

    constructor(address _creatures, address _gold) {
        creatures = CreatureToken(_creatures);
        gold = Gold(_gold);
    }

    function sendToMine(address account, uint256 tokenId) external {
        require(account == msg.sender, "account passed in is not sender");
        require(
            creatures.ownerOf(tokenId) == msg.sender,
            "message sender isn't owner of creature"
        );
        // check approval
        require(
            creatures.getApproved(tokenId) == address(this),
            "staking contract not approved for token"
        );
        // transfer to token to mine contract
        creatures.transferFrom(msg.sender, address(this), tokenId);

        mine[tokenId] = Stake({
            owner: account,
            tokenId: uint16(tokenId),
            value: uint80(block.timestamp)
        });
        totalPlayerStaked += 1;
        emit TokenStaked(account, tokenId, block.timestamp);
    }

    function claimFromMine(uint256 tokenId, bool unstake)
        external
        _updateEarnings
    {
        Stake memory stake = mine[tokenId];
        require(stake.owner == msg.sender, "message sender isn't token owner");
        uint256 owed;
        if (totalGoldEarned < MAX_MINABLE_GOLD) {
            owed = ((block.timestamp - stake.value) * DAILY_GOLD_RATE) / 1 days;
        } else if (stake.value > lastClaimTimestamp) {
            owed = 0; // gold production stopped already
        } else {
            owed =
                ((lastClaimTimestamp - stake.value) * DAILY_GOLD_RATE) /
                1 days; // stop earning gold if it's all been earned
        }

        // mint gold to claimer accordingly
        gold.mint(_msgSender(), owed);

        if (unstake) {
            creatures.safeTransferFrom(address(this), msg.sender, tokenId);
            delete mine[tokenId];
            totalPlayerStaked -= 1;
        } else {
            mine[tokenId] = Stake({
                owner: msg.sender,
                tokenId: uint16(tokenId),
                value: uint80(block.timestamp)
            }); // reset stake timer
        }
        emit TokenClaimed(tokenId, owed, unstake);
    }

    modifier _updateEarnings() {
        if (totalGoldEarned < MAX_MINABLE_GOLD) {
            totalGoldEarned +=
                ((block.timestamp - lastClaimTimestamp) *
                    totalPlayerStaked *
                    DAILY_GOLD_RATE) /
                1 days;
            lastClaimTimestamp = block.timestamp;
        }
        _;
    }

    function onERC721Received(
        address,
        address from,
        uint256,
        bytes calldata
    ) external pure override returns (bytes4) {
      require(from == address(0x0), "Cannot send tokens to mine directly");
      return IERC721Receiver.onERC721Received.selector;
    }
}
