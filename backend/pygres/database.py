from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL di connessione al database PostgreSQL
DATABASE_URL = "postgresql://Hackathon2024:Hackathon2024@postgres:5432/db_Hackathon2024"

# Crea l'engine di connessione
engine = create_engine(DATABASE_URL, echo=True)

# SessionLocal è una factory per ottenere sessioni di connessione
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base per i modelli
Base = declarative_base()
