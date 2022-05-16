// SPDX-License-Identifier: MIT
pragma solidity 0.8.9;

/// @title A dwarf factory
/// @author bushwalker.eth
contract DwarfFactory {
    uint dnaDigits = 16;
    uint dnaModulus = 10 ** dnaDigits;

    struct Dwarf {
        string name;
        uint dna;
    }

    Dwarf[] public dwarfs;

    // function createDwarf (string memory _name, uint _dna) public {
    //     dwarfs.push(Dwarf(_name, _dna));
    // }

    function createRandomDwarf(string memory _name) public {
        uint randDna = _generateRandomDna(_name);
        _createDwarf(_name, randDna);
    }


    function _createDwarf (string memory _name, uint _dna) private {
        dwarfs.push(Dwarf(_name, _dna));
    }

    function _generateRandomDna(string memory _str) private view returns (uint) {
        uint rand = uint(keccak256(abi.encodePacked(_str))); // TODO: Replace with chainlink
        return rand % dnaModulus;
    }
}
