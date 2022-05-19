from brownie import DwarfToken, chain


def test_mint(user, dwarfs):
    dwarfs.publicMint('Gabriele', {"from":user})
    assert dwarfs.totalSupply() == 1
    assert dwarfs.balanceOf(user) == 1
