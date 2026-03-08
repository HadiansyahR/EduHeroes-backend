from pydantic import BaseModel

class RoleCreate(BaseModel):
    role_name: str

class RoleRead(BaseModel):
    id_role: int
    role_name: str

    class Config:
        from_attributes = True