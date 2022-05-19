from brownie import chain


def test_createRandomGoblin(admin, goblin_factory):

    goblin_factory.createRandomGoblin("Duzz")
    assert goblin_factory.goblins(0) == ("Duzz", 45894985)
    assert goblin_factory.goblinToOwner(0) == admin
