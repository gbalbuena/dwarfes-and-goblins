import pytest
from brownie import Wei


def test_mint(gold, admin, user):
    gold.mint(user.address, Wei("1 ether"), {"from": admin })
    assert gold.balanceOf(user.address) == Wei("1 ether")


def test_mint_unauthorized(gold, admin, user):
    gold.mint(user.address, Wei("1 ether"), {"from": user })
    assert gold.balanceOf(user.address) == Wei("1 ether")
