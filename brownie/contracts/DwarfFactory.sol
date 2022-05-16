// SPDX-License-Identifier: MIT
pragma solidity 0.8.9;

/// @title A dwarf factory
/// @author bushwalker.eth
contract DwarfFactory {
    event NewDwarf(uint dwarfId, string name, uint dna);
    
    uint dnaDigits = 16;
    uint dnaModulus = 10 ** dnaDigits;

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
        dwarfs.push(Dwarf(_name, _dna));
        uint id = dwarfs.length - 1;
        dwarfToOwner[id] = msg.sender;
        ownerDwarfCount[msg.sender]++;
        emit NewDwarf(id, _name, _dna);
    }

    // TODO: Replace with chainlink
    function _generateRandomDna(string memory _str) private view returns (uint) {
        uint rand = uint(keccak256(abi.encodePacked(_str)));
        return rand % dnaModulus;
    }
}
