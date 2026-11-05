from src.main.api.foundation.endpoint import Endpoint
from src.main.api.foundation.requesters.crud_requester import CrudRequester
from src.main.api.foundation.requesters.validate_crud_requester import ValidateCrudRequester
from src.main.api.models.create_account_response import CreateAccountResponse
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.models.credit_repay_request import CreditRepayRequest
from src.main.api.models.credit_request_request import CreditRequestRequest
from src.main.api.models.credit_user_request import CreditUserRequest
from src.main.api.models.deposit_account_request import DepositAccountRequest
from src.main.api.models.transfer_account_request import TransferAccountRequest
from src.main.api.specs.request_specs import RequestSpecs
from src.main.api.specs.response_specs import ResponseSpecs
from src.main.api.steps.base_steps import BaseSteps


class UserSteps(BaseSteps):
    def create_account(self, credit_user_request: CreditUserRequest):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(username=credit_user_request.username, password=credit_user_request.password),
            Endpoint.CREATE_ACCOUNT,
            ResponseSpecs.request_created()
        ).post()
        return response

    def create_account_extra_invalid(self, credit_user_request: CreditUserRequest):
        response = CrudRequester(
            RequestSpecs.auth_headers(username=credit_user_request.username, password=credit_user_request.password),
            Endpoint.CREATE_ACCOUNT_EXTRA,
            ResponseSpecs.request_conflict()
        ).post()
        return response

    def credit_request(self, credit_user_request: CreditUserRequest, credit_request_request: CreditRequestRequest):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(username=credit_user_request.username, password=credit_user_request.password),
            Endpoint.CREDIT_REQUEST,
            ResponseSpecs.request_created()
        ).post(credit_request_request)
        return response

    def credit_request_invalid(self, credit_user_request: CreditUserRequest, credit_request_request: CreditRequestRequest):
        response = CrudRequester(
            RequestSpecs.auth_headers(username=credit_user_request.username, password=credit_user_request.password),
            Endpoint.CREDIT_REQUEST_INVALID,
            ResponseSpecs.request_bad()
        ).post(credit_request_request)
        return response

    def credit_repay_request(self, credit_user_request: CreditUserRequest, credit_repay_request: CreditRepayRequest):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(username=credit_user_request.username, password=credit_user_request.password),
            Endpoint.CREDIT_REPAY_REQUEST,
            ResponseSpecs.request_ok()
        ).post(credit_repay_request)
        return response

    def credit_repay_request_invalid(self, credit_user_request: CreditUserRequest, credit_repay_request: CreditRepayRequest):
        response = CrudRequester(
            RequestSpecs.auth_headers(username=credit_user_request.username, password=credit_user_request.password),
            Endpoint.CREDIT_REPAY_REQUEST_INVALID,
            ResponseSpecs.request_unprocessable()
        ).post(credit_repay_request)
        return response

    def deposit_account_request(self, create_user_request: CreateUserRequest, deposit_account_request: DepositAccountRequest):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            Endpoint.DEPOSIT_ACCOUNT_REQUEST,
            ResponseSpecs.request_ok()
        ).post(deposit_account_request)
        return response

    def deposit_account_request_invalid(self, create_user_request: CreateUserRequest, deposit_account_request: DepositAccountRequest):
        response = CrudRequester(
            RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            Endpoint.DEPOSIT_ACCOUNT_REQUEST_INVALID,
            ResponseSpecs.request_bad()
        ).post(deposit_account_request)
        return response

    def transfer_account_request(self, create_user_request: CreateUserRequest, transfer_account_request: TransferAccountRequest):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            Endpoint.TRANSFER_ACCOUNT_REQUEST,
            ResponseSpecs.request_ok()
        ).post(transfer_account_request)
        return response

    def transfer_account_request_invalid(self, create_user_request: CreateUserRequest, transfer_account_request: TransferAccountRequest):
        response = CrudRequester(
            RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            Endpoint.TRANSFER_ACCOUNT_REQUEST_INVALID,
            ResponseSpecs.request_bad()
        ).post(transfer_account_request)
        return response