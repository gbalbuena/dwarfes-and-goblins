// SPDX-License-Identifier: MIT
pragma solidity 0.8.9;

contract CreatureDescriptor {
    function parts(uint256 dna_) public pure returns (uint256, uint256, uint256, uint256) {
        uint256 attr1 = dna_ % 100000000 / 1000000;
        uint256 attr2 = dna_ % 1000000 / 10000;
        uint256 attr3 = dna_ % 10000 / 100;
        uint256 attr4 = dna_ % 100;
        return (attr1, attr2, attr3, attr4);
    }
}
