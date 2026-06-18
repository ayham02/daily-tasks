from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/student/{id}")
async def get_student(id: int):
    return {"student_id": id}