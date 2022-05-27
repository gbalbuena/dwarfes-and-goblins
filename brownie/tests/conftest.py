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

from scripts.helpful_scripts import (
    get_account,
    get_contract,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
    listen_for_event,
)

from scripts.vrf_scripts.create_subscription import (
    create_subscription,
    fund_subscription,
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
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
            pytest.skip("Only for local testing")
    # Arrange
    account = get_account()
    subscription_id = create_subscription()
    fund_subscription(subscription_id=subscription_id)
    gas_lane = config["networks"][network.show_active()][
        "gas_lane"
    ]  # Also known as keyhash
    vrf_coordinator = get_contract("vrf_coordinator")
    link_token = get_contract("link_token")
    nft = admin.deploy(CreatureToken, opensea_proxy, vrf_coordinator.address, subscription_id, gas_price=chain.base_fee)
    nft.requestRandomWords()
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
