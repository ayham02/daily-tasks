from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class StudentCreate(BaseModel):
    name: str
    age: int = Field(gt=18, description="Age must be greater than 18")
    email: EmailStr
    course: str
    phone_number: str

class StudentUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = Field(default = None,gt = 18)
    email : Optional[EmailStr] = None
    course: Optional[str] = None
    phone_number: Optional[str] = None