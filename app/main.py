from fastapi import FastAPI
from sqlalchemy.orm import Session

import models
from db import engine, SessionLocal
from fastapi import Depends
import crud

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {"Ahoy": "Captain"}

@app.post("/create_friend")
def create_friend(first_name: str, last_name: str, age: int, db: Session = Depends(get_db)):
    friend = crud.create_friend(db=db, first_name=first_name, last_name=last_name, age=age)
    return {"friend": friend}

@app.get("/list_friends")
def list_friends(db:Session = Depends(get_db)):
    friends_list = crud.list_friends(db=db)
    return friends_list

@app.put("/update_friend/{id}/")
def update_friend(id:int, first_name:str, last_name:str, age:int, db:Session=Depends(get_db)):
    db_friend = crud.get_friend(db=db, id=id)
    if db_friend:
        update_friend = crud.update_friends(db=db, id=id, first_name=first_name, last_name=last_name, age=age)
        return update_friend
    else:
        return {"error": f"Friend with id {id} does not exist"}

@app.delete("/delete_friend/{id}/")
def delete_friend(id:int, db:Session=Depends(get_db)):
    db_friend = crud.get_friend(db=db, id=id)
    if db_friend:
        return crud.delete_friend(db=db, id=id)
    else:
        return {"error": f"Friend with id {id} does not exist"}



