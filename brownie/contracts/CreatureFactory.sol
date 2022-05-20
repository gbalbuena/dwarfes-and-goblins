// SPDX-License-Identifier: MIT
pragma solidity 0.8.9;

/// @title A dwarf factory
/// @author bushwalker.eth
/// Factory and storage
contract CreatureFactory {
    event NewCreature(uint256 creatureId, string name, uint256 dna);

    uint256 public constant MAX_SUPPLY = 1000;

    uint256 dnaDigits = 8;
    uint256 dnaModulus = 10 ** dnaDigits;

    struct Creature {
        string name;
        uint256 dna;
    }

    Creature[] public creatures;
    mapping (uint256 => address) public creaturesToOwner;
    mapping (address => uint256) ownerCreaturesCount;

    function createRandomCreature(string memory _name) public {
        uint256 randDna = _generateRandomDna(_name);
        _createCreature(_name, randDna);
    }

    function _createCreature(string memory _name, uint256 _dna) internal {
        require(creatures.length <= MAX_SUPPLY, "Maximum supply reached");
        creatures.push(Creature(_name, _dna));
        uint256 id = creatures.length - 1;
        creaturesToOwner[id] = msg.sender;
        ownerCreaturesCount[msg.sender]++;
        emit NewCreature(id, _name, _dna);
    }

    function _generateRandomDna(string memory _str) internal view returns (uint256) {
        uint256 rand = uint256(keccak256(abi.encodePacked(_str)));
        return rand % dnaModulus;
    }
}
