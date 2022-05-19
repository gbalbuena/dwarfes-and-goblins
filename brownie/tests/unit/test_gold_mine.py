import pytest
from brownie import chain, Wei


def test_staking(gold_mine, dwarfs_minted, user):
    dwarfs = dwarfs_minted
    # set approval
    dwarfs.approve(gold_mine.address, 0, {"from": user})
    # test staking
    gold_mine.sendToMine(user, 0, {"from": user})

    assert dwarfs.balanceOf(gold_mine.address) == 1
    assert dwarfs.balanceOf(user) == 0

    # print(f"chain time : {chain.time()}")
    # chain.sleep(86400)
    # print(f"chain time : {chain.time()}")

    # # test unstaking
    # gold_mine.claimFromMine(0, True, {"from": user, "gas_price": chain.base_fee})
    # print(f"balance : {gold.balanceOf(user)}")

    # assert dwarfs.balanceOf(gold_mine.address) == 0
    # assert dwarfs.balanceOf(user) == 1
    # assert gold.balanceOf(user) == Wei(20, "ether")

    # # test stake again
    # # set approval
    # dwarfs.approve(gold_mine.address, 0, {"from": user, "gas_price": chain.base_fee})
    # # test staking
    # gold_mine.sendToMine(user, 0, {"from": user, "gas_price": chain.base_fee})

    # assert dwarfs.balanceOf(gold_mine.address) == 1
    # assert dwarfs.balanceOf(user) == 0

    # print(f"chain time : {chain.time()}")
    # chain.sleep(86400)
    # print(f"chain time : {chain.time()}")

    # # test harvest, but leave nft in mine
    # gold_mine.claimFromMine(0, False, {"from": user, "gas_price": chain.base_fee})
    # print(f"balance : {gold.balanceOf(user)}")

    # assert dwarfs.balanceOf(gold_mine.address) == 1
    # assert dwarfs.balanceOf(user) == 0
    # assert gold.balanceOf(user) == Wei(40, "ether")
