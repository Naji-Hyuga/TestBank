from enum import StrEnum


class TransactionType(StrEnum):
    DEPOSIT = "deposit"
    CREDIT_REPAYMENT = "credit_repayment"
    CREDIT_ISSUANCE = "credit_issuance"
    TRANSFER = "transfer"