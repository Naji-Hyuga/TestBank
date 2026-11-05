from enum import StrEnum


class UserRole(StrEnum):
    ROLE_USER = "ROLE_USER"
    ROLE_CREDIT = "ROLE_CREDIT_SECRET"
    ROLE_ADMIN = "ROLE_ADMIN"