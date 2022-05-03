import pytest
from brownie import NftGame, Contract, chain
from brownie.network import priority_fee


def test_blacklistDeployment(opensea_proxy, dev_account):
    priority_fee("2 gwei")
    nft_game = dev_account.deploy(NftGame, opensea_proxy, gas_price=chain.base_fee)
    assert nft_game.name() == "NftGame"