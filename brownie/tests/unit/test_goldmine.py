import pytest
from brownie import DwarfsAndGoblinsToken, Gold, Mine, Contract, chain
from scripts.helpful_scripts import (get_account)
from brownie.network import priority_fee

def test_deployment():
    priority_fee("2 gwei")
    admin = get_account()
    minter = get_account(index=1)
    mock = get_account(index=2)
    # test deployment
    nft = admin.deploy(DwarfsAndGoblinsToken, mock.address, gas_price=chain.base_fee)
    gold = admin.deploy(Gold, gas_price=chain.base_fee)
    mine = admin.deploy(Mine, nft.address, gold.address, gas_price=chain.base_fee)

def test_minting():
    minter = get_account(index=1)
    nft = DwarfsAndGoblinsToken[-1]
    priority_fee("2 gwei")
    nft.publicMint("test", {"from": minter, "gas_price": chain.base_fee})
    
    assert nft.balanceOf(minter) == 1

def test_staking():

    mine = Mine[-1]
    gold = Gold[-1]
    nft = DwarfsAndGoblinsToken[-1]
    admin = get_account()
    minter = get_account(index=1)
    # set approval
    nft.approve(mine.address, 0, {"from": minter, "gas_price": chain.base_fee})
    # test staking
    mine.sendToMine(minter, 0, {"from": minter, "gas_price": chain.base_fee})

    assert nft.balanceOf(mine.address) == 1
    assert nft.balanceOf(minter) == 0

    # before unstaking must initialize minter as a controller
    tx = gold.addController(minter.address, {"from": admin, "gas_price": chain.base_fee})
    tx.wait(1)

    # test unstaking
    mine.claimFromMine(0, True, {"from": minter, "gas_price": chain.base_fee})

    assert nft.balanceOf(mine.address) == 0
    assert nft.balanceOf(minter) == 1


