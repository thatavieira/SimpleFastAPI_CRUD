from fastapi import FastAPI
import models
from db import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def home():
    return {"Ahoy": "Captain"}
