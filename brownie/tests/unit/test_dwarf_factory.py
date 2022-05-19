from brownie import DwarfFactory, Contract, chain
from brownie.network import priority_fee


def test_createRandomDwarf(admin, dwarf_factory):
    dwarf_factory.createRandomDwarf("Nabbi")
    assert dwarf_factory.dwarfs(0) == ("Nabbi", 80053153)
    assert dwarf_factory.dwarfToOwner(0) == admin
