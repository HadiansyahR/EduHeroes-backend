from pydantic import BaseModel, EmailStr, Field

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str = Field(..., min_length=8, max_length=72)
    role_id: int

class UserRead(BaseModel):
    username: str
    email: EmailStr
    role_id: int
    is_active: bool

    class Config:
        from_attributes = True