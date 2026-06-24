from sqlalchemy import Column, Integer, String
from schemas import StudentCreate
from database import Base
from pydantic import Field

class Student(Base):
    __tablename__ = "students"

    student_id = Column(Integer, primary_key=True, index=True)
    s_name = Column(String(100), nullable=False)
    age = Column(Integer, nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    course = Column(String(100), nullable=False)
    phone = Column(String(15), unique=True, index=True, nullable=False)

class UserRegistration(StudentCreate):
    s_name : str
    age : int = Field(gt=18)
    is_acticve : bool = True

    