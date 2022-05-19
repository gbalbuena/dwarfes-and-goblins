import pytest
import os
import json

from brownie import (
    DwarfFactory,
    DwarfMetadata,
    DwarfToken,
    GoblinFactory,
    chain,
    network,
    config,accounts
)

from scripts.helpful_scripts import (
    LOCAL_BLOCKCHAIN_ENVIRONMENTS
)

@pytest.fixture
def opensea_proxy():
    yield config["networks"][network.show_active()]["openseaProxy"]

@pytest.fixture
def nft_game(dev_account, opensea_proxy):
    nft = dev_account.deploy(
        DwarfFactory,
        DwarfMetadata,
        DwarfToken,
        GoblinFactory,
        opensea_proxy,
        gas_price=chain.base_fee
    )
    yield nft

@pytest.fixture
def dev_account():
    return accounts[0]

@pytest.fixture
def admin():
    return accounts[0]

@pytest.fixture
def user():
    return accounts[1]
