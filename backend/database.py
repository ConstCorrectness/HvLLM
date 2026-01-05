from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Use the config that works (Port 5433)
DB_USER = "admin"
DB_PASS = "password123"
DB_HOST = "localhost"
DB_NAME = "hvllm"
DB_PORT = "5433" 

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()