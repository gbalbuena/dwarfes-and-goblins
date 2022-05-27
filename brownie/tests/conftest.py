from dataclassy import factory
import pytest
import os
import json

from brownie import (
    CreatureFactory,
    CreatureToken,
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
def mine(admin, creatures, gold):
    mine = admin.deploy(Mine, creatures, gold, gas_price=chain.base_fee)
    yield mine

@pytest.fixture
def creature_factory(admin):
    factory = admin.deploy(CreatureFactory, gas_price=chain.base_fee)
    yield factory

@pytest.fixture
def creatures(admin, opensea_proxy, subscriptionId):
    nft = admin.deploy(CreatureToken, opensea_proxy, subscriptionId, gas_price=chain.base_fee)
    yield nft

@pytest.fixture
def creatures_minted(creatures, user):
    creatures.publicMint('Gabriele', {"from":user})
    assert creatures.balanceOf(user) == 1
    yield creatures

@pytest.fixture
def subscriptionId():
    subId = config["networks"][network.show_active()]["subscriptionId"]
    return subId

@pytest.fixture
def admin():
    return accounts[0]

@pytest.fixture
def user():
    return accounts[1]

@pytest.fixture
def mock_user():
    return accounts[1]
