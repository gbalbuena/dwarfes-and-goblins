#!/usr/bin/python3
from time import sleep
from brownie import NftGame , accounts, network, config, chain
from brownie.network import priority_fee
from scripts.helpful_scripts import get_publish_source

def main():
    priority_fee(2)
    dev_account = accounts[0]
    opensea_proxy = config["networks"][network.show_active()]["openseaProxy"]
    metadata_baseUri = config["networks"][network.show_active()]["metadata"]
    
    print(network.show_active())
    creat00r = dev_account.deploy(NftGame, opensea_proxy, gas_price=chain.base_fee, publish_source=get_publish_source())
    creat00r.setIsPublicSaleActive(True, {"from":dev_account})
    creat00r.setBaseURI(metadata_baseUri, {"from": dev_account})
