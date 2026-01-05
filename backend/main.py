from fastapi import FastAPI
from sqlalchemy import create_engine, text
from redis import Redis
import os
import time
from contextlib import asynccontextmanager

# --- CONFIGURATION (Matches docker-compose.yml) ---
DB_USER = "admin"
DB_PASS = "password123"
DB_HOST = "localhost"
DB_NAME = "hvllm"
DB_PORT = "5433"

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Global connection objects
engine = None
redis_client = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    global engine, redis_client
    print("\n--- 🚀 HvLLM BACKEND RESTART ---")
    
    # 1. Test Postgres
    try:
        engine = create_engine(DATABASE_URL)
        with engine.connect() as conn:
            # We fetch the current user to prove auth works
            res = conn.execute(text("SELECT current_user")).fetchone()
            print(f"✅ Postgres: CONNECTED as '{res[0]}'")
    except Exception as e:
        print(f"❌ Postgres: FAILED - {e}")

    # 2. Test Redis
    try:
        redis_client = Redis(host='localhost', port=6379, decode_responses=True)
        redis_client.ping()
        print("✅ Redis:    CONNECTED")
    except Exception as e:
        print(f"❌ Redis:    FAILED - {e}")
    
    print("--------------------------------\n")
    yield
    if engine:
        engine.dispose()

app = FastAPI(lifespan=lifespan)

@app.get("/")
def read_root():
    return {"status": "Online"}