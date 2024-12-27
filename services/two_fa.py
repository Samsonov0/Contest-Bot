import pyotp


class TwoFactorAuth:
    def __init__(self, secret_key: str = pyotp.random_base32()):
        self.secret_key = secret_key
        self.totp = pyotp.TOTP(self.secret_key)

    def get_secret_key(self):
        return self.secret_key

    def verify_code(self, code):
        return self.totp.verify(code)
