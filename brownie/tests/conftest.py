from dataclassy import factory
import pytest
import os
import json

from brownie import (
    DwarfFactory,
    DwarfMetadata,
    DwarfToken,
    GoblinFactory,
    Gold,
    Mine,
    chain,
    network,
    config,accounts
)
from brownie.network import priority_fee, connect
connect()
priority_fee("2 gwei")

@pytest.fixture
def opensea_proxy():
    yield config["networks"][network.show_active()]["openseaProxy"]

@pytest.fixture
def gold(admin):
    gold = admin.deploy(Gold)
    yield gold

@pytest.fixture
def gold_mine(admin, dwarfs, gold):
    mine = admin.deploy(Mine, dwarfs, gold, gas_price=chain.base_fee)
    yield mine

@pytest.fixture
def dwarf_factory(admin):
    factory = admin.deploy(DwarfFactory, gas_price=chain.base_fee)
    yield factory

@pytest.fixture
def goblin_factory(admin):
    factory = admin.deploy(GoblinFactory, gas_price=chain.base_fee)
    yield factory

@pytest.fixture
def dwarfs(admin, opensea_proxy):
    nft = admin.deploy(DwarfToken, opensea_proxy, gas_price=chain.base_fee)
    yield nft

@pytest.fixture
def dwarfs_minted(dwarfs, user):
    dwarfs.publicMint('Gabriele', {"from":user})
    assert dwarfs.balanceOf(user) == 1
    yield dwarfs

@pytest.fixture
def goblins(admin, opensea_proxy):
    nft = admin.deploy(DwarfToken, opensea_proxy, gas_price=chain.base_fee)
    yield nft

@pytest.fixture
def admin():
    return accounts[0]

@pytest.fixture
def user():
    return accounts[1]

@pytest.fixture
def mock_user():
    return accounts[1]
