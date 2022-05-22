import pytest
from brownie import CreatureFactory, CreatureToken, Gold, Mine, chain, Wei


def test_creature_token_deployment(admin, opensea_proxy):
    game = admin.deploy(CreatureToken, opensea_proxy, gas_price=chain.base_fee)
    assert game.name() == "Creatures"


def test_gold_Deployment(admin):
    gold = admin.deploy(Gold, gas_price=chain.base_fee)
    assert gold.name() == "GOLD"


def test_mine_Deployment(admin, gold, creatures):
    mine = admin.deploy(Mine, creatures.address, gold.address, gas_price=chain.base_fee)
    assert mine.DAILY_GOLD_RATE() == Wei('20 ether')


def test_creature_factory(admin):
    df = admin.deploy(CreatureFactory, gas_price=chain.base_fee)
