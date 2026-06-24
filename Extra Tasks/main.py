import mysql.connector as mc
from pydantic import BaseModel, Field, EmailStr
from fastapi import FastAPI
from typing import Optional

app = FastAPI()

class StudentCreate(BaseModel):
    name: str
    age: int = Field(ge=18, description="Age must be greater than or equal to 18")
    email: EmailStr
    course: str
    phone: str


class StudentUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    email: Optional[EmailStr] = None
    course: Optional[str] = None
    phone: Optional[str] = None

co = mc.connect(host='localhost',port=3306,user='root',password='root',database='intern_db')
cursor = co.cursor()

@app.get("/")
def home():
    return {"message": "Hello"}

@app.get("/students/{student_id}")
def get_student_by_id_api(student_id: int):

    cursor.execute("Select * from students where student_id = %s",(student_id,))
    data = cursor.fetchone()

    if data is None:
        return {"message":"Student Not Found"}
    
    return {
    "student_id": data[0],
    "name": data[1],
    "age": data[2],
    "email": data[3],
    "course": data[4],
    "phone": data[5]
    }

@app.get("/allstudents")
def get_all_students():
    cursor.execute("Select * from students")
    dataa = cursor.fetchall()

    if not dataa:
        return {"message" : "Table empty"}
    
    result = []

    for data in dataa:
        result.append({"student_id": data[0],
    "name": data[1],
    "age": data[2],
    "email": data[3],
    "course": data[4],
    "phone": data[5]})
        
    return result

@app.post("/createstudents")
def create_students(student:StudentCreate):

    
    query = """
        insert into students
        (s_name, age, email, course, phone)
        values
        (%s,%s,%s,%s,%s)    
"""
    values = (student.name,student.age,student.email,student.course,student.phone)
    cursor.execute(query,values)
    co.commit()

    return {"message" : "Student Created Successfully",
            "student_id" : cursor.lastrowid}

@app.put("/updatestudents/{student_id}")
def update_students(student:StudentUpdate,student_id:int):
    cursor.execute("select * from students where student_id = %s",(student_id,))
    a1 = cursor.fetchone()
    if a1 is None:
        return {"Message":"Student not found"}
    
    if student.name is None:
        student.name = a1[1]
    if student.age is None:
        student.age = a1[2]
    if student.email is None:
        student.email = a1[3]
    if student.course is None:
        student.course = a1[4]
    if student.phone is None:
        student.phone = a1[5]

    query = """
        update students
        set
            s_name = %s,
            age = %s,
            email = %s,
            course = %s,
            phone = %s
        where student_id = %s
"""
    values = (student.name,student.age,student.email,student.course,student.phone,student_id)
    cursor.execute(query,values)
    co.commit()
    return {"Message":"Student updated succesfully"}

@app.delete("/deletestudents/{student_id}")
def delete_student(student_id:int):
    cursor.execute("select * from students where student_id =%s",(student_id,))
    a1 = cursor.fetchone()
    if not a1:
        return {"Message":"Student Not Found"}
    cursor.execute("delete from students where student_id = %s",(student_id,))
    co.commit()
    return {"Message":"Student deleted succesfully"}