#!/usr/bin/python3
from time import sleep
from brownie import accounts, network, config, chain, DwarfToken, Wei
from brownie.network import priority_fee
from scripts.helpful_scripts import get_publish_source, get_account

def main():
    priority_fee(2)
    dev_account = get_account()
    opensea_proxy = config["networks"][network.show_active()]["openseaProxy"]
    # metadata_baseUri = config["networks"][network.show_active()]["metadata"]
    
    print(network.show_active())
    creat00r = dev_account.deploy(DwarfToken, opensea_proxy, 4749, gas_price=Wei('6 gwei'), publish_source=True)
    print(f"dwarf deployed at {creat00r}")
    # creat00r.setIsPublicSaleActive(True, {"from":dev_account})
    # creat00r.setBaseURI(metadata_baseUri, {"from": dev_account})
