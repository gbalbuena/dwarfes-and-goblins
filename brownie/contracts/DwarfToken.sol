// SPDX-License-Identifier: MIT
pragma solidity 0.8.9;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/interfaces/IERC2981.sol";
import "@openzeppelin/contracts/interfaces/IERC20.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import { IProxyRegistry } from './../external/opensea/IProxyRegistry.sol';

import "./DwarfFactory.sol";

contract DwarfToken is Ownable, ReentrancyGuard, ERC721Enumerable, DwarfFactory {
    IProxyRegistry public immutable proxyRegistry;
    constructor(IProxyRegistry _openSeaProxyRegistryAddress) ERC721("Dwarfs", "DWA") {
        proxyRegistry = _openSeaProxyRegistryAddress;
    }

    function publicMint(string memory _name) public {
        createRandomDwarf(_name);
    }
}
