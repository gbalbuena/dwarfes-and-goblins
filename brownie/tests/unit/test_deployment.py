import pytest
from brownie import CreatureFactory, CreatureToken, Gold, Mine, chain, config, network, Wei, ZERO_ADDRESS

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

def test_creature_token_deployment(admin, opensea_proxy, subscriptionId):
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
            pytest.skip("Only for local testing")
    # Arrange
    subscription_id = create_subscription()
    fund_subscription(subscription_id=subscription_id)
    gas_lane = config["networks"][network.show_active()][
        "gas_lane"
    ]  # Also known as keyhash
    vrf_coordinator = get_contract("vrf_coordinator")
    link_token = get_contract("link_token")
    game = admin.deploy(CreatureToken, opensea_proxy, subscription_id,
        vrf_coordinator,
        link_token,
        gas_lane,  # Also known as keyhash
        gas_price=chain.base_fee)
    assert game.name() == "Creatures"


def test_gold_Deployment(admin):
    gold = admin.deploy(Gold, gas_price=chain.base_fee)
    assert gold.name() == "GOLD"


def test_mine_Deployment(admin, gold, creatures):
    mine = admin.deploy(Mine, creatures.address, gold.address, gas_price=chain.base_fee)
    assert mine.DAILY_GOLD_RATE() == Wei('20 ether')


def test_creature_factory(admin):
    df = admin.deploy(CreatureFactory, gas_price=chain.base_fee)
