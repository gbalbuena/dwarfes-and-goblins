// SPDX-License-Identifier: MIT
pragma solidity 0.8.9;

/// @title A dwarf factory
/// @author bushwalker.eth
/// @author anotherme.eth
/// Factory and storage
contract CreatureFactory {
    event NewCreature(uint256 creatureId, string name, Race race, uint256 dna);

    uint256 public constant MAX_SUPPLY = 1000;

    uint256 dnaDigits = 8;
    uint256 dnaModulus = 10 ** dnaDigits;

    struct Creature {
        string name;
        Race race;
        uint256 dna;
    }

    enum Race {
        Dwarf,
        Goblin
    }

    Creature[] public creatures;
    mapping (uint256 => address) public creaturesToOwner;
    mapping (address => uint256) ownerCreaturesCount;

    function createRandomCreature(string memory _name) public {
        uint256 randDna = _generateRandomDna(_name);
        _createCreature(_name, Race.Dwarf, randDna);
    }

    function _createCreature(string memory name_, Race race_, uint256 dna_) internal {
        require(creatures.length <= MAX_SUPPLY, "Maximum supply reached");
        creatures.push(Creature(name_, race_, dna_));
        uint256 id = creatures.length - 1;
        creaturesToOwner[id] = msg.sender;
        ownerCreaturesCount[msg.sender]++;
        emit NewCreature(id, name_, race_, dna_);
    }

    function _generateRandomDna(string memory _str) internal view returns (uint256) {
        uint256 rand = uint256(keccak256(abi.encodePacked(_str)));
        return rand % dnaModulus;
    }
}
