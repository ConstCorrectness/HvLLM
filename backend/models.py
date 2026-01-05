from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, JSON
from sqlalchemy.dialects.postgresql import UUID
from database import Base
import uuid
import datetime

class Match(Base):
    __tablename__ = "matches"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    environment = Column(String, index=True)
    player_human_id = Column(String)
    player_agent_id = Column(String)
    started_at = Column(DateTime, default=datetime.datetime.utcnow)
    winner = Column(String, nullable=True)

class MoveLog(Base):
    __tablename__ = "move_logs"
    # In TimescaleDB, time is the primary index
    time = Column(DateTime, primary_key=True, default=datetime.datetime.utcnow)
    match_id = Column(UUID(as_uuid=True), ForeignKey("matches.id"), primary_key=True)
    actor = Column(String)
    action_type = Column(String)
    payload = Column(JSON) # Stores flexible data: {"move": "e4"} or {"chat": "hi"}
    thinking_time_ms = Column(Integer)