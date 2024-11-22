from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
import models
from Database import SessionLocal, engine

# Creazione delle tabelle
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency per il database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/")
def create_user(username: str, password_hash: str, db: Session = Depends(get_db)):
    # Verifica se l'utente esiste già
    db_user = db.query(models.User).filter(models.User.username == username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")

    # Creazione nuovo utente
    user = models.User(username=username, password_hash=password_hash)
    db.add(user)
    db.commit()
    db.refresh(user)  # Ricarica i dati dall'ID appena creato
    return user

@app.get("/users/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    # Cerca l'utente per ID
    user = db.query(models.User).filter(models.User.uid == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
