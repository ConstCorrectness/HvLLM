from fastapi import FastAPI
from sqlalchemy import create_engine, text
from redis import Redis
import os
import time
from contextlib import asynccontextmanager


from database import engine, Base
from models import Match, MoveLog

# --- CONFIGURATION (Matches docker-compose.yml) ---
DB_USER = "admin"
DB_PASS = "password123"
DB_HOST = "localhost"
DB_NAME = "hvllm"
DB_PORT = "5433"

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("\n--- 🚀 HvLLM INITIALIZING SCHEMA ---")
    
    # 1. Create Standard Tables (matches, move_logs)
    Base.metadata.create_all(bind=engine)
    print("✅ Standard Tables Created")

    # 2. Convert 'move_logs' to a Hypertable (TimescaleDB magic)
    with engine.connect() as conn:
        try:
            # This SQL command turns the table into a time-series optimized hypertable
            conn.execute(text("SELECT create_hypertable('move_logs', 'time', if_not_exists => TRUE);"))
            conn.commit()
            print("✅ Hypertable 'move_logs' Configured")
        except Exception as e:
            print(f"⚠️ Hypertable warning (might already exist): {e}")
            
    print("------------------------------------\n")
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/")
def read_root():
    return {"status": "HvLLM Schema Ready", "db": "Active"}