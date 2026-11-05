import pytest

from src.main.api.classes.api_manager import ApiManager
from src.main.api.fake_data.fake_data_generate import FakeDataGenerate
from src.main.api.generators.model_generator import RandomModelGenerator
from src.main.api.models.create_account_response import CreateAccountResponse
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.models.credit_request_request import CreditRequestRequest
from src.main.api.models.credit_user_request import CreditUserRequest
from src.main.api.models.login_user_request import LoginUserRequest


@pytest.fixture
def create_user_request(api_manager: ApiManager):
    user_request = RandomModelGenerator.generate(CreateUserRequest)
    api_manager.admin_steps.create_user(user_request)
    return user_request

@pytest.fixture
def credit_user_request(api_manager: ApiManager):
    user_request = RandomModelGenerator.generate(CreditUserRequest)
    api_manager.admin_steps.create_user(user_request)
    return user_request

@pytest.fixture
def credit_login_user_request(credit_user_request: CreditUserRequest):
    return LoginUserRequest(
        username=credit_user_request.username,
        password=credit_user_request.password
    )

@pytest.fixture
def create_account_request(api_manager: ApiManager, credit_user_request: CreditUserRequest):
    response = api_manager.user_steps.create_account(credit_user_request)
    return response


@pytest.fixture
def credit_request_fix(api_manager: ApiManager, credit_user_request: CreditUserRequest, create_account_request):
    credit_request = CreditRequestRequest(accountId=create_account_request.id)
    response = api_manager.user_steps.credit_request(credit_user_request, credit_request)
    return response

@pytest.fixture
def wrong_password_login_user_request(create_user_request: CreateUserRequest):
    return LoginUserRequest(
        username=create_user_request.username,
        password=FakeDataGenerate.wrong_password()
    )


