from brownie import DwarfFactory, Contract, chain
from brownie.network import priority_fee

def test_dwarf_factory(dev_account):
    priority_fee("2 gwei")
    df = dev_account.deploy(DwarfFactory, gas_price=chain.base_fee)
    df.createRandomDwarf('Nabbi')
    assert df.dwarfs(0) == ("Nabbi", 9687977680053153)
    assert  df.dwarfToOwner(0) == dev_account