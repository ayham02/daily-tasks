from fastapi import FastAPI
from models import Student
from database import Base, SessionLocal, engine
from schemas import StudentCreate, StudentUpdate
app = FastAPI()
@app.get("/")
def read_root():
    return {"message": "Welcome to the Student Management API"}

@app.get("/readallstudents")
def read_students():
    db = SessionLocal()
    students = db.query(Student).all()
    db.close()
    return students

@app.post("/createstudents")
def create_students(student:StudentCreate):
    db = SessionLocal()
    db_student = Student(
        s_name = student.name,
        age = student.age,
        email = student.email,
        course = student.course,
        phone = student.phone_number
    )

    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    db.close()

    return {"message" : "Student Created Successfully",
            "student_id" : db_student.student_id}

@app.get("/readstudents/{student_id}")
def read_student(student_id: int):
    db = SessionLocal()
    student = db.query(Student).filter(Student.student_id == student_id).first()
    return student

@app.put("/updatestudents/{student_id}")
def student_update(student_id: int, student: StudentUpdate):
    db = SessionLocal()
    db_student = db.query(Student).filter(Student.student_id == student_id).first()
    if student.name is not None:
        db_student.s_name = student.name
    if student.age is not None:
        db_student.age = student.age
    if student.email is not None:
        db_student.email = student.email
    if student.course is not None:
        db_student.course = student.course
    if student.phone_number is not None:
        db_student.phone = student.phone_number
    db.commit()
    db.refresh(db_student)
    return f"Student with ID {student_id} updated successfully."
    db.close()

@app.delete("/students")
def delete_students(student_id: int):
    db = SessionLocal()
    db_student = db.query(Student).filter(Student.student_id == student_id).first()
    if db_student:
        db.delete(db_student)
        db.commit()
        return f"Student deleted successfully"
    else:
        return f"Student Not Found"