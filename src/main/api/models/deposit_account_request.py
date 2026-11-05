from src.main.api.fake_data.fake_data_generate import FakeDataGenerate
from src.main.api.models.base_model import BaseModel
from pydantic import Field


class DepositAccountRequest(BaseModel):
    accountId: int
    amount: float = Field(default_factory=FakeDataGenerate.amount_deposit)