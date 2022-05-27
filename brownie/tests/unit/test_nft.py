import pytest
from brownie import chain
import brownie
from brownie import CreatureToken, convert, network, config
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


def test_mint(user, creatures):
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

    creatures.publicMint('Gabriele', { "from": user })
    assert creatures.totalSupply() == 1
    assert creatures.balanceOf(user) == 1

def test_mint_failure(user, creatures):
    expected_revert_msg = "Please initalize randomness"
    with brownie.reverts(expected_revert_msg):
        creatures.publicMint('Gabriele', { "from": user })
    assert creatures.totalSupply() == 0
    assert creatures.balanceOf(user) == 0
