from brownie.network.main import priority_fee
import pytest
from brownie import chain, Wei, DwarfToken, Contract
from scripts.helpful_scripts import get_account

def main():
    priority_fee(2)
    account = get_account()
    dwarf = Contract("0xE1051e42cF94e3544943BC67cA04737A3c67C007")
    tx = dwarf.requestRandomWords({"from": account, "gas_price": Wei('1.2 gwei')})
    tx.wait(1)

    print(f"tx : {tx}")