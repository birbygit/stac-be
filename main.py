from typing import Optional
from fastapi import FastAPI
from routers import ticket

app = FastAPI()

app.include_router(ticket.router)
