from brownie import CreatureFactory, Contract, chain
from brownie.network import priority_fee

def test_max_supply(admin, creature_factory):
    assert creature_factory.MAX_SUPPLY() == 1000;

def test_create_random_creature(admin, creature_factory):
    creature_factory.createRandomCreature("Nabbi")
    assert creature_factory.creatures(0)[0] == "Nabbi"
    assert creature_factory.creatures(0)[1] == 0
    # ('Nabbi', 0, 69029877367329498841586387660617)
    assert creature_factory.creaturesToOwner(0) == admin
