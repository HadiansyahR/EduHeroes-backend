from pydantic import BaseModel

class EnrollmentCreate(BaseModel):
    course_id: int

class EnrollmentRead(BaseModel):
    id_enrollment: int
    user_id: int
    course_id: int

    class Config:
        from_attributes = True