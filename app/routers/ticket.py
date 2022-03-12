from .. import models, schemas
from .. import database, oauth2
from fastapi import Depends, Response, status, HTTPException, APIRouter
from sqlalchemy.orm import Session
from typing import List

router = APIRouter(
    prefix = "/tickets",
    tags=['Tickets']
)

@router.get("/", response_model=List[schemas.Ticket])
def get_posts(db: Session = Depends(database.get_db), current_agent: int = Depends(oauth2.get_current_agent)):
    tickets = db.query(models.Ticket).all()
    return tickets