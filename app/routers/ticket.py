from . import models
from fastapi import APIRouter

router = APIRouter(
    prefix = "/tickets",
    tags=['Tickets']
)

@router.get("/", response_model=List[schemas.Ticket])
def get_posts(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    tickets = db.query(models.Ticket).all()
    return tickets