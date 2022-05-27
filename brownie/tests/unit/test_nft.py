import pytest
from brownie import chain
import brownie
from brownie import CreatureToken, convert, network, config


def test_mint(user, creatures_seeded):
    creatures_seeded.publicMint('Gabriele', { "from": user })
    assert creatures_seeded.totalSupply() == 1
    assert creatures_seeded.balanceOf(user) == 1

def test_mint_failure(user, creatures):
    expected_revert_msg = "Please initalize randomness"
    with brownie.reverts(expected_revert_msg):
        creatures.publicMint('Gabriele', { "from": user })
    assert creatures.totalSupply() == 0
    assert creatures.balanceOf(user) == 0
