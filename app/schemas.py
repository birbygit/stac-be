from pydantic import BaseModel, EmailStr
from datetime import date, datetime
from typing import List, Optional

class AgentCreate(BaseModel):
    email : EmailStr
    password : str

class AgentOut(BaseModel):
    id : int
    email : EmailStr
    created_at: datetime

    class Config:
        orm_mode = True

class TicketBase(BaseModel):
    title: str
    content: str

#response class
class Ticket(TicketBase):
    id: int
    agent_id: int
    client_id: int
    status_id: int
    referral_id: int
    created_at: datetime
    agent: AgentOut

    class Config:
        orm_mode = True

#security related
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None
