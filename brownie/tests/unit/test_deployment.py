import pytest
from brownie import GoblinFactory, DwarfFactory, DwarfToken, Gold, Mine, chain, Wei


def test_DwarfToken_Deployment(admin, opensea_proxy):
    game = admin.deploy(DwarfToken, opensea_proxy, gas_price=chain.base_fee)
    assert game.name() == "Dwarfs"


def test_Gold_Deployment(admin):
    gold = admin.deploy(Gold, gas_price=chain.base_fee)
    assert gold.name() == "GOLD"


def test_Mine_Deployment(admin, gold, dwarfs):
    mine = admin.deploy(Mine, dwarfs.address, gold.address, gas_price=chain.base_fee)
    assert mine.DAILY_GOLD_RATE() == Wei('20 ether')


def test_GoblinFactory(admin):
    df = admin.deploy(GoblinFactory, gas_price=chain.base_fee)


def test_DwarfFactory(admin):
    df = admin.deploy(DwarfFactory, gas_price=chain.base_fee)
