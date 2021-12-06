from brownie import FundMe, MockV3Aggregator, network, config
from scripts.helpful_scripts import get_account ,deploy_mocks,LOCAL_BLOCKCHAIN_ENVIRONMENTS

#import os

def deploy_fund_me():
    account = get_account()
    #Publish source code
    #if we are on a persistent network like rinkeby, use the associated address
    # otherwise, deploy mocks
    #if network.show_active() != "development":
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        print("Deploying test dev...")
        price_feed_address = config["networks"][network.show_active()]["eth_usd_price_feed"]
    else:
       deploy_mocks()
       price_feed_address = MockV3Aggregator[-1].address
    
    print("Mocks Deployed!")
    #Developmetn publish_source = False
    fund_me = FundMe.deploy(
                            price_feed_address, 
                            {"from": account} ,
                            publish_source = config["networks"][network.show_active()].get("verify"))
    #fund_me = FundMe.deploy(
    #    price_feed_address,
    #    {"from": account}, 
    #    publish_source = True
    #)
    #print("Contract deployed to {fund_me.address}")
    return fund_me


def main():
    #print(os.getenv("WEB3_INFURA_PROJECT_ID"))
    deploy_fund_me()