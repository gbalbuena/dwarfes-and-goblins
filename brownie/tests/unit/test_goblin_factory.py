from brownie import GoblinFactory, Contract, chain
from brownie.network import priority_fee

def test_goblin_factory(dev_account):
    priority_fee("2 gwei")
    df = dev_account.deploy(GoblinFactory, gas_price=chain.base_fee)
    df.createRandomGoblin('Duzz')
    assert df.goblins(0) == ("Duzz", 45894985)
    assert  df.goblinToOwner(0) == dev_account
