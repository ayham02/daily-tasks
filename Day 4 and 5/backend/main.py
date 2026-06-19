from fastapi import FastAPI
from pydantic import BaseModel, EmailStr, Field

app = FastAPI()

class Student(BaseModel):
    student_id: int
    name: str
    age: int = Field(gt=18, description="Age must be greater than 18")
    email: EmailStr 
    course: str
    phone_number: str


@app.get("/hello")
async def root():
    return {"message": "Hello World"}

@app.get("/student/{id}")
async def get_student(id: int):
    return {"student_id": id}

@app.post("/student/")
async def create_student(student: Student):
    return {"message": "Student created successfully", "student": student}

@app.put("/student/{id}")
async def update_student(id: int, student: Student):
    return {"message": "Student updated successfully", "student_id": id, "student": student}

@app.delete("/student/{id}")
async def delete_student(id: int):
    return {"message": "Student deleted successfully", "student_id": id}