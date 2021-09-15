from brownie import FundMe, MockV3Aggregator, network, config
from scripts.helper import get_account, deploy_mocks, LOCAL_BLOCKCHAIN_ENVIRONMENTS


def deploy_fund_me():
    account = get_account()

    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        price_fedd_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        deploy_mocks()
        price_fedd_address = MockV3Aggregator[-1].address
        print("Mocks Deployed!")

    fund_me = FundMe.deploy(
        price_fedd_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print(f"contrat deployed to  {fund_me.address}")
    return fund_me

def main():
    deploy_fund_me()
