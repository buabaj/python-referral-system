from datetime import datetime
from pydantic import BaseModel, EmailStr


class User(BaseModel):
    first_name: str
    last_name: str
    phone: str
    email: EmailStr
    token: str
    created_at: datetime
    updated_at: datetime
