from sqlalchemy import create_engine
from sqlalchemy.orm  import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

load_dotenv()   # .env fayldan oqiydi

DATABASE_URL = os.getenv("DATABASE_URL")

# Engine -databasega ulanish
engine = create_engine(DATABASE_URL)

#session har bir so`rov uchun
SessionLocal = sessionmaker(autocommmit= False, autoflush=False, bind=engine)

#Base barcha modellar shundan meros oladi
Base = declarative_base()

#dependency har bir endpoint uchun sessiya beradi,ilatilgandan keyin yopadi
def get_db():
    db= SessionLocal()
    try:
        yield db
    finally: 
        db.close()
        