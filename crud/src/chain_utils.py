from xrpl.clients import JsonRpcClient
from xrpl.wallet import Wallet
from xrpl.account import get_balance
from xrpl.models import requests, transactions, Memo
from xrpl.utils import xrp_to_drops
from xrpl.transaction import submit_and_wait, XRPLReliableSubmissionException
from xrpl.utils.str_conversions import hex_to_str, str_to_hex
from os import getenv


client = JsonRpcClient("https://s.altnet.rippletest.net:51234/")


class ChainUtils:
    
    @staticmethod
    def create_account():
        new_wallet = Wallet.create()
        return new_wallet

    @staticmethod
    def get_account(seed=""):
        new_wallet = Wallet.from_seed(seed)
        return new_wallet

    @classmethod
    def get_account_balance(cls, seed: str) -> str:
        account = cls.get_account(seed)
        balance = cls.get_balance(account.address, client)
        return balance

    @classmethod
    def send_transaction(
        cls,
        seed: str,
        receiver: str,
        memo_list: list[str] = None,
    ):
        sending_wallet = cls.get_account(seed)
        payment = transactions.Payment(
            account=sending_wallet.address,
            amount=1,
            destination=receiver,
            memos=(
                [transactions.Memo(memo_data=str_to_hex(memo)) for memo in memo_list]
                if memo_list
                else None
            ),
        )
        try:
            response = submit_and_wait(payment, client, sending_wallet)
            new_balance = get_balance(sending_wallet.address, client)
            print(
                f"Transaction successfully submitted, youre new balance is {new_balance}"
            )
        except Exception as e:
            print(e)
            raise e
        return response

    @staticmethod
    def get_account_info(account: Wallet = None):
        acct_info = requests.AccountInfo(account=account.address, queue=True)
        return client.request(acct_info)

    @staticmethod
    def get_tx(tx_hash: str):
        tx = requests.Tx(transaction=tx_hash)
        response = client.request(tx)
        return response

    def get_txs(address: str):
        request = requests.AccountTx(account=address)
        try:
            response = client.request(request)
            transactions = response.result.get("transactions", [])

            print(transactions[0])

            txs = [tx.get("hash") for tx in transactions]

            return txs

        except Exception as e:
            print(f"Error querying transactions: {e}")

    @staticmethod
    def parse_memo(data):
        return Memo(memo_data=data)


# print(
#     ChainUtils.get_txs(
#         ChainUtils.get_account("sEd76moZfYw12aeUNsq1TpYiJv83iwv").address
#     )
# )
