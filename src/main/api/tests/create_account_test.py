import pytest
from sqlalchemy.orm import Session

from src.main.api.classes.api_manager import ApiManager
from src.main.api.db.crud.account_crud import AccountCrudDb as Account
from src.main.api.models.create_user_request import CreateUserRequest


@pytest.mark.api
class TestCreateAccount:
    def test_create_account(self, api_manager: ApiManager, credit_user_request: CreateUserRequest, db_session: Session):
        response = api_manager.user_steps.create_account(credit_user_request)

        assert response.balance == 0, "Баланса нет, ошибка"

        account_from_db = Account.get_account_by_id(db_session, response.id)

        assert account_from_db.id == response.id, "Аккаунт не создан, id аккаунта нет в БД"
        assert account_from_db.balance is not None, "Поле баланса для созданного аккаунта отсутствует в БД"

    def test_create_account_invalid(self, api_manager: ApiManager, credit_user_request: CreateUserRequest, db_session: Session):
        api_manager.user_steps.create_account(credit_user_request)
        api_manager.user_steps.create_account(credit_user_request)
        api_manager.user_steps.create_account_extra_invalid(credit_user_request)
