from brownie import CreatureToken, chain

def test_mint(user, creatures):
    creatures.publicMint('Gabriele', { "from": user })
    assert creatures.totalSupply() == 1
    assert creatures.balanceOf(user) == 1
