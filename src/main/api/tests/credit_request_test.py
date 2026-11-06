import pytest

from src.main.api.classes.api_manager import ApiManager
from src.main.api.fake_data.fake_data_generate import FakeDataGenerate
from src.main.api.fixtures.api_fixture import api_manager
from src.main.api.models.credit_request_request import CreditRequestRequest
from src.main.api.db.crud.credit_crud import CreditCrudDb as Credit
from sqlalchemy.orm import Session

from src.main.api.models.credit_user_request import CreditUserRequest


@pytest.mark.api
class TestCreditRequest:
    def test_credit_request_valid(self, api_manager: ApiManager, db_session: Session, create_account_request, credit_user_request: CreditUserRequest):
        credit_request = CreditRequestRequest(accountId=create_account_request.id)
        response = api_manager.user_steps.credit_request(credit_user_request, credit_request)

        assert credit_request.accountId == response.id, "Id счета не совпадает"
        assert response.balance == credit_request.amount, "Баланс не изменился, ошибка"

        credit_from_db = Credit.get_credit_by_id(db_session, response.creditId)

        assert credit_from_db.id == response.creditId, "Кредит не создан, id кредита нет в БД"
        assert credit_from_db.amount == response.amount, "Поле сумма для созданного кредита не совпадает"

    def test_credit_request_invalid(self, api_manager: ApiManager, db_session: Session, create_account_request, credit_user_request: CreditUserRequest):
        credit_request = CreditRequestRequest(
            accountId=create_account_request.id,
            amount=FakeDataGenerate.amount_credit_invalid()
        )
        api_manager.user_steps.credit_request_invalid(credit_user_request, credit_request)

        credit_from_db = Credit.get_credit_by_account_id(db_session, create_account_request.id)

        assert credit_from_db is None, "Кредит создан, ошибка"
