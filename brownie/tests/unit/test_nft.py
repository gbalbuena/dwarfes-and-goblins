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


def test_setBaseURI(creatures, admin, base_uri):
    creatures.setBaseURI(base_uri, {"from": admin})
    assert creatures.getBaseURI() == base_uri


def test_contractURI(creatures):
    assert creatures.contractURI() == "ipfs://QmQNdhY8RHi8arMZ58c36pJNDCFHLtomk2qfgMuEtKrDmx"


def test_setContractURIHash(creatures, admin, base_uri):
    creatures.setContractURIHash(base_uri[7:], {"from": admin})
    assert creatures.contractURI() == base_uri


def test_setBaseURI_no_permission(creatures, user):
    before = creatures.getBaseURI()
    expected_revert_msg = "Ownable: caller is not the owner"
    with brownie.reverts(expected_revert_msg):
        creatures.setBaseURI("", {"from": user})
    assert creatures.getBaseURI() == before
