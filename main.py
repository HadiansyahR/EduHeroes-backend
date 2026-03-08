from fastapi import FastAPI
from api.v1.users import router as user_router
from api.v1.roles import router as role_router
app = FastAPI()

app.include_router(user_router, prefix="/api/v1")
app.include_router(role_router, prefix="/api/v1")