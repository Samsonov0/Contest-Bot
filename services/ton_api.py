import base64
from datetime import datetime
from decimal import Decimal
from pprint import pprint
from typing import Union

import requests


class TonAPI:
    def __init__(self):
        self.ton_api_url = 'https://toncenter.com/api/v2/'
        self.api_key = 'f538426bb99cebd2b341595475f0ae12efe1d0cb2c61ff149ad8b2b72a602068'
        self.headers = {
            "X-API-Key": self.api_key
        }


    def nano_to_token(self, nano: Decimal):
        return Decimal(str(nano / Decimal(str(10**9))))

    def token_to_nano(self, token: Decimal):
        return Decimal(str(token * 10**9))

    def get_transactions(self, address: str, limit: int):
        end_point = f'{self.ton_api_url}getTransactions'

        response = requests.get(
            url=end_point,
            params={
                'address': address,
                'limit': limit
            },
            headers=self.headers
        )

        if not response.status_code == 200:
            return

        return response.json().get('result')

    def check_transaction_to_wallet(self, to_wallet: str, amount: Union[int | float | Decimal], memo: str):
        if isinstance(amount, (float, int)):
            amount = Decimal(str(amount))

        transactions = self.get_transactions(
            address=to_wallet,
            limit=50
        )

        for transaction in transactions:
            in_msg = transaction.get('in_msg')

            value = Decimal(in_msg.get('value'))
            message = in_msg.get('message')

            if message.isdigit():
                message = int(message)

            target_value = self.token_to_nano(
                amount
            )

            if message == memo and value >= target_value:
                return True

        return False

# hamster_wallet = 'UQD4KLaYjrbfKu_FwvCpqUlpk0mzdWJ23wLlkCcFz1Nx71hE'
# main_wallet = 'UQCyrdXsM-1Ab_MIryz64Lj1zFIqnAN68HOTPdOdia0wvsvY'

# ton_api = TonAPI()
#
# is_ok = ton_api.check_transaction_to_wallet(
#     # from_wallet='UQD4KLaYjrbfKu_FwvCpqUlpk0mzdWJ23wLlkCcFz1Nx71hE',
#     to_wallet='UQCyrdXsM-1Ab_MIryz64Lj1zFIqnAN68HOTPdOdia0wvsvY',
#     amount=0.1,
#     memo='468154084'
# )
