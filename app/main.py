import imp
from typing import Optional
from fastapi import Depends, FastAPI, Response, status, HTTPException
from fastapi.params import Body
from .import models, schemas, utils
from .database import engine, get_db
from .routers import ticket

models.Base.metadata.create_all(bind=engine)

app = FastAPI() #instance of FastAPI
app.include_router(ticket.router)

@app.get("/") # decorator '@' + app reference + http method-> transform function in API 
def root():  #function plain python  -- name doesn't matter
    return {"message": "Benvenuto in Support! v0.1"} # py dictionary -> JSON