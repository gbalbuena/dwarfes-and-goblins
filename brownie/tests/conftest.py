import pytest

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

from scripts.helpful_scripts import (
    get_account,
    get_contract,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS
)

from scripts.vrf_scripts.create_subscription import (
    create_subscription,
    fund_subscription,
)


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
def creatures_seeded(admin, creatures):
    tx = creatures.requestRandomWords()
    tx.wait(1)
    request_id = tx.events[0]["requestId"]
    assert isinstance(request_id, int)
    vrf_coordinator = get_contract("vrf_coordinator")
    vrf_coordinator.fulfillRandomWords(
        request_id, creatures.address, {"from": get_account()}
    )
    yield creatures

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
    nft = admin.deploy(CreatureToken, opensea_proxy, subscription_id,
        vrf_coordinator,
        link_token,
        gas_lane,  # Also known as keyhash
        gas_price=chain.base_fee)

    yield nft

@pytest.fixture
def creatures_minted(creatures_seeded, user):
    creatures_seeded.publicMint('Gabriele', {"from":user})
    assert creatures_seeded.balanceOf(user) == 1
    yield creatures_seeded

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
