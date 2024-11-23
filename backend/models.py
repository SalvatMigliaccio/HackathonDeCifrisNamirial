from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

# Crea la base per i modelli
Base = declarative_base()

# Modello User
class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)  # Cambio da uid a id
    username = Column(String(255), unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    email = Column(String(255), unique=True, nullable=False)  # Aggiunta del campo email

    # Relazioni con altre tabelle
    pratiche = relationship("Pratica", back_populates="user")
    documenti = relationship("Documento", back_populates="user")


# Modello Operatore
class Operatore(Base):
    __tablename__ = "operatori"
    
    id = Column(Integer, primary_key=True, index=True)  # Cambio da uid a id
    username = Column(String(255), unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    email = Column(String(255), unique=True, nullable=False)  # Aggiunta del campo email

    # Relazione con gruppi
    gruppi = relationship("OperatoreGruppo", back_populates="operatore")


# Modello Gruppo
class Gruppo(Base):
    __tablename__ = "gruppi"
    
    id = Column(Integer, primary_key=True, index=True)  # Cambio da uid a id
    group_name = Column(String(255), nullable=False)
    parent_group_id = Column(Integer, ForeignKey('gruppi.id', ondelete="SET NULL"), nullable=True)

    # Relazione al gruppo genitore
    parent_group = relationship("Gruppo", remote_side=[id])

    # Relazione con operatori
    operatori = relationship("OperatoreGruppo", back_populates="gruppo")


# Modello Pratica
class Pratica(Base):
    __tablename__ = "pratica"
    
    id = Column(Integer, primary_key=True, index=True)  # Cambio da practice_id a id
    wallet_address = Column(String(255), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)  # Cambio da uid a id

    # Relazione con l'utente
    user = relationship("User", back_populates="pratiche")


# Modello Documento
class Documento(Base):
    __tablename__ = "documento"
    
    id = Column(Integer, primary_key=True, index=True)  # Cambio da doc_id a id
    hash = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)  # Cambio da uid a id
    redirect_uri = Column(String, nullable=True)

    # Relazione con l'utente
    user = relationship("User", back_populates="documenti")


# Modello OperatoreGruppo
class OperatoreGruppo(Base):
    __tablename__ = "operatoregruppo"
    
    operator_id = Column(Integer, ForeignKey('operatori.id', ondelete="CASCADE"), primary_key=True)  # Cambio da uid a id
    group_id = Column(Integer, ForeignKey('gruppi.id', ondelete="CASCADE"), primary_key=True)  # Cambio da uid a id

    # Relazioni
    operatore = relationship("Operatore", back_populates="gruppi")
    gruppo = relationship("Gruppo", back_populates="operatori")
