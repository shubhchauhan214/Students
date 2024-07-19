from typing import Annotated
from fastapi import FastAPI, Depends, HTTPException, Path
from sqlalchemy.orm import Session
from starlette import status

from models import Students
import models
from database import engine, SessionLocal

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


# Get All Data
@app.get("/", status_code=status.HTTP_200_OK)
async def read_all(db: db_dependency):
    return db.query(Students).all()


# Read data using id
@app.get("/student/{student_id}", status_code=status.HTTP_200_OK)
async def student_by_id(db: db_dependency, student_id: int = Path(gt=0)):
    student_model = db.query(Students).filter(Students.id == student_id).first()
    if student_model is not None:
        return student_model
    raise HTTPException(status_code=404, detail='Student not found')


