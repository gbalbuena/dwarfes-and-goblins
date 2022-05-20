import pytest
from brownie import chain, Wei


def test_staking(mine, gold, creatures_minted, user):
    creatures = creatures_minted
    # set approval
    creatures.approve(mine.address, 0, { "from": user })
    # test staking
    mine.sendToMine(user, 0, { "from": user })

    assert creatures.balanceOf(mine.address) == 1
    assert creatures.balanceOf(user) == 0

    print(f"chain time : {chain.time()}")
    chain.sleep(86400)
    print(f"chain time : {chain.time()}")

    # test unstaking
    mine.claimFromMine(0, True, {"from": user, "gas_price": chain.base_fee})
    print(f"balance : {gold.balanceOf(user)}")

    assert creatures.balanceOf(mine.address) == 0
    assert creatures.balanceOf(user) == 1
    assert gold.balanceOf(user) == Wei("20 ether")

    # test stake again
    # set approval
    creatures.approve(mine.address, 0, {"from": user, "gas_price": chain.base_fee})
    # test staking
    mine.sendToMine(user, 0, {"from": user, "gas_price": chain.base_fee})

    assert creatures.balanceOf(mine.address) == 1
    assert creatures.balanceOf(user) == 0

    print(f"chain time : {chain.time()}")
    chain.sleep(86400)
    print(f"chain time : {chain.time()}")

    # test harvest, but leave nft in mine
    mine.claimFromMine(0, False, {"from": user, "gas_price": chain.base_fee})
    print(f"balance : {gold.balanceOf(user)}")

    assert creatures.balanceOf(mine.address) == 1
    assert creatures.balanceOf(user) == 0
    assert gold.balanceOf(user) == Wei("40 ether")
