from datetime import datetime
from pydantic import BaseModel
from typing import Optional

class CreateUserDto(BaseModel):
    telegram_user_id: int
    first_name: str
    last_name: Optional[str]
    username: Optional[str]
    language_code: str
    integration_code: Optional[str]
    created_at: datetime


class ResponseUserDto(BaseModel):
    id: int
    telegram_user_id: int
    first_name: str
    last_name: Optional[str]
    username: Optional[str]
    language_code: str
    integration_code: Optional[str]
    created_at: datetime
