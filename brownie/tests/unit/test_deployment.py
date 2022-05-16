import pytest
from brownie import DwarfsAndGoblinsToken, Contract, chain
from brownie.network import priority_fee


def test_blacklistDeployment(opensea_proxy, dev_account):
    priority_fee("2 gwei")
    game = dev_account.deploy(DwarfsAndGoblinsToken, opensea_proxy, gas_price=chain.base_fee)
    assert game.name() == "Dwarfs and Goblins"
