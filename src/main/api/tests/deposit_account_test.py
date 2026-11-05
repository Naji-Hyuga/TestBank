import pytest

from src.main.api.classes.api_manager import ApiManager
from src.main.api.constants.transaction_type import TransactionType
from src.main.api.fake_data.fake_data_generate import FakeDataGenerate
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.models.credit_user_request import CreditUserRequest
from src.main.api.models.deposit_account_request import DepositAccountRequest
from sqlalchemy.orm import Session
from src.main.api.db.crud.transaction_crud import TransactionCrudDb as Transaction




@pytest.mark.api
class TestDepositAccount:
    def test_deposit_account_valid(self, api_manager: ApiManager, db_session: Session, create_account_request, credit_user_request: CreditUserRequest):
        deposit_account_request = DepositAccountRequest(accountId=create_account_request.id)
        response = api_manager.user_steps.deposit_account_request(credit_user_request, deposit_account_request)

        assert deposit_account_request.accountId == response.id
        assert deposit_account_request.amount == response.balance

        transaction_from_db = Transaction.get_transaction_by_to_account_id(db_session, response.id)

        assert transaction_from_db.transaction_type == TransactionType.DEPOSIT, "Счет не пополнен, ошибка "



    def test_deposit_account_invalid(self, api_manager: ApiManager, db_session: Session, create_account_request, credit_user_request: CreditUserRequest):
        deposit_account_request = DepositAccountRequest(
            accountId=create_account_request.id,
            amount=FakeDataGenerate.amount_deposit_invalid()
        )
        api_manager.user_steps.deposit_account_request_invalid(credit_user_request, deposit_account_request)

        transaction_from_db = Transaction.get_transaction_by_to_account_id(db_session, deposit_account_request.accountId)

        assert transaction_from_db is None, "Счет пополнен, ошибка"
