from dataclasses import dataclass
from enum import Enum
from typing import Optional, Type

from src.main.api.models.base_model import BaseModel
from src.main.api.models.create_account_response import CreateAccountResponse
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.models.create_user_response import CreateUserResponse
from src.main.api.models.credit_repay_request import CreditRepayRequest
from src.main.api.models.credit_repay_response import CreditRepayResponse
from src.main.api.models.credit_request_request import CreditRequestRequest
from src.main.api.models.credit_request_response import CreditRequestResponse
from src.main.api.models.deposit_account_request import DepositAccountRequest
from src.main.api.models.deposit_account_response import DepositAccountResponse
from src.main.api.models.login_user_request import LoginUserRequest
from src.main.api.models.login_user_response import LoginUserResponse
from src.main.api.models.transfer_account_request import TransferAccountRequest
from src.main.api.models.transfer_account_response import TransferAccountResponse


@dataclass
class EndpointConfiguration:
    url: str
    request_model: Optional[Type[BaseModel]]
    response_model: Optional[Type[BaseModel]]


class Endpoint(Enum):
    ADMIN_CREATE_USER = EndpointConfiguration(
        request_model = CreateUserRequest,
        url = "/admin/create",
        response_model = CreateUserResponse
    )

    ADMIN_DELETE_USER = EndpointConfiguration(
        request_model = None,
        url = "/admin/users",
        response_model = None
    )

    LOGIN_USER = EndpointConfiguration(
        request_model = LoginUserRequest,
        url = "/auth/token/login",
        response_model=LoginUserResponse
    )

    CREATE_ACCOUNT = EndpointConfiguration(
        request_model = None,
        url = "/account/create",
        response_model = CreateAccountResponse
    )

    CREATE_ACCOUNT_EXTRA = EndpointConfiguration(
        request_model=None,
        url="/account/create",
        response_model=None
    )

    CREDIT_REQUEST = EndpointConfiguration(
        request_model = CreditRequestRequest,
        url= "/credit/request",
        response_model = CreditRequestResponse
    )

    CREDIT_REQUEST_INVALID = EndpointConfiguration(
        request_model = CreditRequestRequest,
        url= "/credit/request",
        response_model = None
    )

    CREDIT_REPAY_REQUEST = EndpointConfiguration(
        request_model = CreditRepayRequest,
        url="/credit/repay",
        response_model = CreditRepayResponse
    )

    CREDIT_REPAY_REQUEST_INVALID = EndpointConfiguration(
        request_model = CreditRepayRequest,
        url="/credit/repay",
        response_model = None
    )

    DEPOSIT_ACCOUNT_REQUEST = EndpointConfiguration(
        request_model = DepositAccountRequest,
        url="/account/deposit",
        response_model = DepositAccountResponse
    )

    DEPOSIT_ACCOUNT_REQUEST_INVALID = EndpointConfiguration(
        request_model = DepositAccountRequest,
        url="/account/deposit",
        response_model = None
    )

    TRANSFER_ACCOUNT_REQUEST = EndpointConfiguration(
        request_model = TransferAccountRequest,
        url="/account/transfer",
        response_model = TransferAccountResponse
    )

    TRANSFER_ACCOUNT_REQUEST_INVALID = EndpointConfiguration(
        request_model = TransferAccountRequest,
        url="/account/transfer",
        response_model = None
    )