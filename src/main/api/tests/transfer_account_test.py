import pytest

from src.main.api.classes.api_manager import ApiManager
from src.main.api.constants.transaction_type import TransactionType
from src.main.api.fake_data.fake_data_generate import FakeDataGenerate
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.models.credit_user_request import CreditUserRequest
from src.main.api.models.deposit_account_request import DepositAccountRequest
from src.main.api.models.transfer_account_request import TransferAccountRequest
from sqlalchemy.orm import Session
from src.main.api.db.crud.transaction_crud import TransactionCrudDb as Transaction


@pytest.mark.api
class TestTransferAccount:
    def test_transfer_account_valid(self, api_manager: ApiManager, db_session: Session, create_account_request, credit_user_request: CreditUserRequest):
        deposit_account_request = DepositAccountRequest(accountId=create_account_request.id)
        api_manager.user_steps.deposit_account_request(credit_user_request, deposit_account_request)
        create_another_account_response = api_manager.user_steps.create_account(credit_user_request)

        transfer_account_request = TransferAccountRequest(
            fromAccountId=create_account_request.id,
            toAccountId=create_another_account_response.id,
                amount=deposit_account_request.amount
        )
        response = api_manager.user_steps.transfer_account_request(credit_user_request, transfer_account_request)

        assert transfer_account_request.fromAccountId == response.fromAccountId
        assert transfer_account_request.toAccountId == response.toAccountId
        assert response.fromAccountIdBalance == deposit_account_request.amount - transfer_account_request.amount

        transaction_from_db = Transaction.get_transaction_by_from_account_id(db_session, transfer_account_request.fromAccountId)

        assert transaction_from_db.transaction_type == TransactionType.TRANSFER, "Транзакция не найдена, ошибка"


    def test_transfer_account_invalid(self, api_manager: ApiManager, db_session: Session, create_account_request, credit_user_request: CreditUserRequest):
        deposit_account_request = DepositAccountRequest(accountId=create_account_request.id)
        api_manager.user_steps.deposit_account_request(credit_user_request, deposit_account_request)
        create_another_account_response = api_manager.user_steps.create_account(credit_user_request)

        transfer_account_request = TransferAccountRequest(
            fromAccountId=create_account_request.id,
            toAccountId=create_another_account_response.id,
            amount=FakeDataGenerate.amount_transfer_invalid()
        )
        api_manager.user_steps.transfer_account_request_invalid(credit_user_request, transfer_account_request)

        transaction_from_db = Transaction.get_transaction_by_from_account_id(db_session,
                                                                           transfer_account_request.fromAccountId)

        assert transaction_from_db is None, "Транзакция найдена, ошибка"