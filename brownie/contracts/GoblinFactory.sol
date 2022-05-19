// SPDX-License-Identifier: MIT
pragma solidity 0.8.9;

/// @title A goblin factory
/// @author bushwalker.eth
/// Factory and storage
contract GoblinFactory {
    event NewGoblin(uint goblinId, string name, uint dna);

    uint dnaDigits = 8;
    uint dnaModulus = 10 ** dnaDigits;
    uint constant MAX_SUPPLY = 10000;

    struct Goblin {
        string name;
        uint dna;
    }

    Goblin[] public goblins;
    mapping (uint => address) public goblinToOwner;
    mapping (address => uint) ownerGoblinCount;

    function createRandomGoblin(string memory _name) public {
        uint randDna = _generateRandomDna(_name);
        _createGoblin(_name, randDna);
    }

    function _createGoblin(string memory _name, uint _dna) private {
        require(goblins.length <= MAX_SUPPLY, "Maximum supply reached");
        goblins.push(Goblin(_name, _dna));
        uint id = goblins.length - 1;
        goblinToOwner[id] = msg.sender;
        ownerGoblinCount[msg.sender]++;
        emit NewGoblin(id, _name, _dna);
    }

    function _generateRandomDna(string memory _str) private view returns (uint) {
        uint rand = uint(keccak256(abi.encodePacked(_str)));
        return rand % dnaModulus;
    }
}
