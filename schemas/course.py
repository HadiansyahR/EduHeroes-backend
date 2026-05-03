from pydantic import BaseModel

class CourseCreate(BaseModel):
    course_name: str
    description: str

class CourseRead(BaseModel):
    id_course: int
    course_name: str
    description: str
    created_by: int

    class Config:
        from_attributes = True

class CourseUpdate(BaseModel):
    course_name: str | None = None
    description: str | None = None
