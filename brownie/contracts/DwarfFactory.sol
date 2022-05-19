// SPDX-License-Identifier: MIT
pragma solidity 0.8.9;

/// @title A dwarf factory
/// @author bushwalker.eth
/// Factory and storage
contract DwarfFactory {
    event NewDwarf(uint256 dwarfId, string name, uint256 dna);

    uint256 dnaDigits = 8;
    uint256 dnaModulus = 10 ** dnaDigits;
    uint256 constant MAX_SUPPLY = 1000;

    struct Dwarf {
        string name;
        uint256 dna;
    }

    Dwarf[] public dwarfs;
    mapping (uint256 => address) public dwarfToOwner;
    mapping (address => uint256) ownerDwarfCount;

    function createRandomDwarf(string memory _name) public {
        uint256 randDna = _generateRandomDna(_name);
        _createDwarf(_name, randDna);
    }

    function _createDwarf(string memory _name, uint256 _dna) internal {
        require(dwarfs.length <= MAX_SUPPLY, "Maximum supply reached");
        dwarfs.push(Dwarf(_name, _dna));
        uint256 id = dwarfs.length - 1;
        dwarfToOwner[id] = msg.sender;
        ownerDwarfCount[msg.sender]++;
        emit NewDwarf(id, _name, _dna);
    }

    function _generateRandomDna(string memory _str) internal view returns (uint256) {
        uint256 rand = uint256(keccak256(abi.encodePacked(_str)));
        return rand % dnaModulus;
    }
}
