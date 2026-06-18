from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):
    student_id: int
    name: str
    age: int
    email: str
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