from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from Database import SessionLocal, engine
import models

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

# Crea un nuovo utente
@app.post("/users/")
def create_user(username: str, password_hash: str, email: str, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.username == username).first()  # Cambio da models.user a models.User
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")

    # Creazione dell'utente con email
    user = models.User(username=username, password_hash=password_hash, email=email)  # Cambio da models.user a models.User
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

# Ottieni un utente per ID
@app.get("/users/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()  # Cambio da models.user.uid a models.User.id
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# Crea un nuovo operatore
@app.post("/operatori/")
def create_operatore(username: str, password_hash: str, email: str, db: Session = Depends(get_db)):
    db_operatore = db.query(models.Operatore).filter(models.Operatore.username == username).first()  # Cambio da models.operatore a models.Operatore
    if db_operatore:
        raise HTTPException(status_code=400, detail="Username already registered")

    # Creazione dell'operatore con email
    operatore = models.Operatore(username=username, password_hash=password_hash, email=email)  # Cambio da models.operatore a models.Operatore
    db.add(operatore)
    db.commit()
    db.refresh(operatore)
    return operatore

# Ottieni un operatore per ID
@app.get("/operatori/{operator_id}")
def get_operatore(operator_id: int, db: Session = Depends(get_db)):
    operatore = db.query(models.Operatore).filter(models.Operatore.id == operator_id).first()  # Cambio da models.operatore.uid a models.Operatore.id
    if not operatore:
        raise HTTPException(status_code=404, detail="Operatore not found")
    return operatore
