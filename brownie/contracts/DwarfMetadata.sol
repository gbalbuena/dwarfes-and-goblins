// SPDX-License-Identifier: MIT
pragma solidity 0.8.9;

contract DwarfMetadata {
    // string[] attr1;
    function attributes(uint256 dna) public pure returns (uint256, uint256, uint256, uint256) {
        uint256 a1 = dna % 100000000 / 1000000;
        uint256 a2 = dna % 1000000 / 10000;
        uint256 a3 = dna % 10000 / 100;
        uint256 a4 = dna % 100;
        return (a1, a2, a3, a4);
    }
}
