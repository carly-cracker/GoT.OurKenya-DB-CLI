import sqlite3
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from lib.schema import SCHEMA_SQL

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATABASE_PATH = os.path.join(BASE_DIR, "GoTourKenyaDB.db")
DATABASE_URL = f"sqlite:///{DATABASE_PATH}"

engine = create_engine(DATABASE_URL, echo=False)
Session = sessionmaker(bind=engine)

Base = declarative_base()

def init_db():
    conn = sqlite3.connect(DATABASE_PATH) 
    cursor = conn.cursor()
    cursor.executescript(SCHEMA_SQL)

    conn.commit()
    conn.close()
    
    Base.metadata.create_all(engine)