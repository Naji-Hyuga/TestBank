import pytest
from src.main.api.classes.api_manager import ApiManager
from src.main.api.db.crud.credit_crud import CreditCrudDb as Credit
from src.main.api.fake_data.fake_data_generate import FakeDataGenerate
from src.main.api.models.credit_repay_request import CreditRepayRequest
from src.main.api.models.credit_request_request import CreditRequestRequest
from sqlalchemy.orm import Session

from src.main.api.models.credit_user_request import CreditUserRequest


@pytest.mark.api
class TestCreditRepay:
    def test_credit_repay_valid(
            self, api_manager: ApiManager,
            credit_user_request: CreditUserRequest,
            db_session: Session,
            credit_request_fix: CreditRequestRequest,
            create_account_request,
    ):
        repay_request = CreditRepayRequest(
            creditId=credit_request_fix.creditId,
            accountId=create_account_request.id,
            amount=credit_request_fix.amount
        )
        response = api_manager.user_steps.credit_repay_request(credit_user_request, repay_request)

        assert repay_request.creditId == response.creditId
        assert repay_request.amount == response.amountDeposited

        credit_from_db = Credit.get_credit_by_id(db_session, response.creditId)

        assert credit_from_db.id == response.creditId, "Кредит не создан, id кредита нет в БД"
        assert credit_from_db.amount == response.amountDeposited, "Поле сумма для созданного кредита не совпадает"


    def test_credit_repay_invalid(
            self, api_manager: ApiManager,
            credit_user_request: CreditUserRequest,
            db_session: Session,
            credit_request_fix: CreditRequestRequest,
            create_account_request,
    ):
        repay_request = CreditRepayRequest(
            creditId=credit_request_fix.creditId,
            accountId=create_account_request.id,
            amount=FakeDataGenerate.amount_credit_invalid()
        )
        api_manager.user_steps.credit_repay_request_invalid(credit_user_request, repay_request)

        credit_from_db = Credit.get_credit_by_id(db_session, credit_request_fix.creditId)

        assert credit_from_db.balance == -(credit_request_fix.balance)



