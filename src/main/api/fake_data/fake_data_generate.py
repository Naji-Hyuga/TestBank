import random
import uuid


class FakeDataGenerate:

    @staticmethod
    def amount_credit():
        return round(random.uniform(5000, 15000), 2)

    @staticmethod
    def term_month_credit():
        return random.randint(1, 12)

    @staticmethod
    def amount_credit_invalid():
        return random.choice([4999, 15001])

    @staticmethod
    def amount_deposit():
        return round(random.uniform(1000, 9000), 2)

    @staticmethod
    def amount_deposit_invalid():
        return random.choice([999, 9001])

    @staticmethod
    def wrong_password():
        return str(uuid.uuid4())[:7]

    @staticmethod
    def amount_transfer_invalid():
        return random.choice([499, 10001])