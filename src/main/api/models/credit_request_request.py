import random
from typing import Annotated

from pydantic import Field

from src.main.api.fake_data.fake_data_generate import FakeDataGenerate
from src.main.api.generators.creation_rule import CreationRule
from src.main.api.models.base_model import BaseModel


class CreditRequestRequest(BaseModel):
    accountId: int
    amount: float = Field(default_factory=FakeDataGenerate.amount_credit)
    termMonths: int =  Field(default_factory=FakeDataGenerate.term_month_credit)

