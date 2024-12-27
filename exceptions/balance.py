class InsufficientFundsException(Exception):
    def __init__(self, message):
        super().__init__(message)


class NegativeBalanceException(Exception):
    def __init__(self, message):
        super().__init__(message)


class WalletBalanceNotFoundException(Exception):
    def __init__(self, message):
        super().__init__(message)


