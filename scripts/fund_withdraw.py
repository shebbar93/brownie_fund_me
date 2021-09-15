from brownie import FundMe
from scripts.helper import get_account


def fundme():
    fund_me = FundMe[-1]
    account = get_account()
    enterance_fee = fund_me.getEntranceFee()
    print(f"The current entry fee is {enterance_fee}")
    print("Funding")
    fund_me.fund({"from":account, 'value' : enterance_fee})

def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    print("Withdraw")
    fund_me.withdraw({"from":account})

def main():
    fundme()
    withdraw()