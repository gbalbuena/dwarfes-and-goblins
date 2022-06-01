from brownie.network.main import priority_fee
import pytest
from brownie import chain, Wei, CreatureToken, network, config
from scripts.helpful_scripts import get_account
import time

def test_rinkeby():
    if network.show_active() == "rinkeby":
        account = get_account()
        dwarf = CreatureToken.at("0xE1051e42cF94e3544943BC67cA04737A3c67C007")
        tx = dwarf.requestRandomWords({"from": account, "gas_price": Wei('1.2 gwei')})
        tx.wait(1)
        print(f"tx : {tx}")


