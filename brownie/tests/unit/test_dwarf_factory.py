from brownie import DwarfFactory, Contract, chain
from brownie.network import priority_fee

def test_dwarf_factory(dev_account):
    priority_fee("2 gwei")
    dwarf_factory = dev_account.deploy(DwarfFactory, gas_price=chain.base_fee)
    dwarf_factory.createRandomDwarf('Nabbi')
    assert dwarf_factory.dwarfs(0) == ("Nabbi", 9687977680053153)
    # assert dwarf_factory.name() == "DwarfFactory"