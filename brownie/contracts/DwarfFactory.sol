// SPDX-License-Identifier: MIT
pragma solidity 0.8.9;

/// @title A dwarf factory
/// @author bushwalker.eth
/// Factory and storage
contract DwarfFactory {
    event NewDwarf(uint dwarfId, string name, uint dna);
    
    uint dnaDigits = 8;
    uint dnaModulus = 10 ** dnaDigits;
    uint constant MAX_SUPPLY = 1000;

    struct Dwarf {
        string name;
        uint dna;
    }

    Dwarf[] public dwarfs;
    mapping (uint => address) public dwarfToOwner;
    mapping (address => uint) ownerDwarfCount;

    function createRandomDwarf(string memory _name) public {
        uint randDna = _generateRandomDna(_name);
        _createDwarf(_name, randDna);
    }

    function _createDwarf(string memory _name, uint _dna) private {
        require(dwarfs.length <= MAX_SUPPLY, "Maximum supply reached");
        dwarfs.push(Dwarf(_name, _dna));
        uint id = dwarfs.length - 1;
        dwarfToOwner[id] = msg.sender;
        ownerDwarfCount[msg.sender]++;
        emit NewDwarf(id, _name, _dna);
    }

    function _generateRandomDna(string memory _str) private view returns (uint) {
        uint rand = uint(keccak256(abi.encodePacked(_str)));
        return rand % dnaModulus;
    }
}
