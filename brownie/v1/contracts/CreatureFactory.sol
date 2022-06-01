// SPDX-License-Identifier: MIT
pragma solidity 0.8.9;

error MaximumSupplyReached();

contract CreatureFactory {
    event NewCreature(uint256 creatureId, string name, Race race, uint256 dna);

    uint256 public constant MAX_SUPPLY = 1000;

    uint256 dnaDigits = 32;
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

    function createRandomCreature(string memory _name, uint256 seed) public {
        uint256 randomDna = _generateRandomDna(seed);
        _createCreature(_name, Race.Dwarf, randomDna);
    }

    function _generateRandomDna(uint256 seed) internal view returns (uint256) {
        return seed % dnaModulus;
    }

    function _createCreature(string memory name_, Race race_, uint256 dna_) internal {
        if (creatures.length >= MAX_SUPPLY) {
            revert MaximumSupplyReached(); // Maximum supply reached
        }
        creatures.push(Creature(name_, race_, dna_));
        uint256 tokenId = creatures.length - 1;
        creaturesToOwner[tokenId] = msg.sender;
        ownerCreaturesCount[msg.sender]++;
        emit NewCreature(tokenId, name_, race_, dna_);
    }
}
