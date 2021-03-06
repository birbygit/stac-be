from pickle import TRUE
from .database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, column, null
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship

class Agent(Base):
    __tablename__="agents"
    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable = False, unique = True)
    password = Column(String, nullable = False)
    created_at = Column(TIMESTAMP(timezone=TRUE), server_default=text('now()'), nullable=False)

class Status(Base):
    __tablename__="status"
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    
class Client(Base):
    __tablename__ = "clients"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    address = Column(String, nullable=False)
    zip_code = Column(String, nullable=False)
    country = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=TRUE), server_default=text('now()'), nullable=False)
    updated_at = Column(TIMESTAMP(timezone=TRUE), server_default=text('now()'), nullable=False)
    website_url = Column(String, nullable=True)
    global_mail = Column(String, nullable=True)
    phone_number = Column(String, nullable=True)
    fax_number = Column(String, nullable=True)

class Referral(Base):
    __tablename__="referrals"
    id = Column(Integer, primary_key=True, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable = False)
    client_id = Column(Integer, ForeignKey("clients.id",ondelete="SET NULL"), nullable=False)

    client = relationship("Clients")

class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    agent_id = Column(Integer, ForeignKey("agents.id", ondelete="CASCADE"), nullable=False)
    client_id = Column(Integer, ForeignKey("clients.id",ondelete="SET NULL"), nullable=False)
    referral_id = Column(Integer, ForeignKey("referrals.id", ondelete="SET NULL"), nullable=False)
    status_id = Column(Integer, ForeignKey("status.id", ondelete="SET NULL"), nullable=False)
    created_at = Column(TIMESTAMP(timezone=TRUE), server_default=text('now()'), nullable=False)

    agent = relationship("Agents")
    client = relationship("Clients")
    referral = relationship("Referrals")
    status = relationship("Status")