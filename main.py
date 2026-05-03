from fastapi import FastAPI
from api.v1.users import router as user_router
from api.v1.roles import router as role_router
from api.v1.auth import router as auth_router
from api.v1.courses import router as course_router
from api.v1.enrollments import router as enrollment_router

app = FastAPI()

app.include_router(user_router, prefix="/api/v1")
app.include_router(role_router, prefix="/api/v1")
app.include_router(auth_router, prefix="/api/v1")
app.include_router(course_router, prefix="/api/v1")
app.include_router(enrollment_router, prefix="/api/v1")