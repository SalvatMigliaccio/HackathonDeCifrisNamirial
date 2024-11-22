from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    
    uid = Column(Integer, primary_key=True, index=True)
    username = Column(String(255), unique=True, nullable=False)
    password_hash = Column(String, nullable=False)

    # relazioni
    pratiche = relationship("Pratica", back_populates="user")
    documenti = relationship("Documento", back_populates="user")


class Operatore(Base):
    __tablename__ = "operatori"
    
    uid = Column(Integer, primary_key=True, index=True)
    username = Column(String(255), unique=True, nullable=False)
    password_hash = Column(String, nullable=False)

    # relazioni
    gruppi = relationship("OperatoreGruppo", back_populates="operatore")


class Gruppo(Base):
    __tablename__ = "gruppi"
    
    uid = Column(Integer, primary_key=True, index=True)
    group_name = Column(String(255), nullable=False)
    parent_group_id = Column(Integer, ForeignKey('gruppi.uid', ondelete="SET NULL"), nullable=True)

    # relazione al gruppo genitore
    parent_group = relationship("Gruppo", remote_side=[uid])

    # relazione con operatoregruppo
    operatori = relationship("OperatoreGruppo", back_populates="gruppo")


class Pratica(Base):
    __tablename__ = "pratica"
    
    practice_id = Column(Integer, primary_key=True, index=True)
    wallet_address = Column(String(255), nullable=False)
    user_id = Column(Integer, ForeignKey('users.uid'), nullable=False)

    # relazioni
    user = relationship("User", back_populates="pratiche")


class Documento(Base):
    __tablename__ = "documento"
    
    doc_id = Column(Integer, primary_key=True, index=True)
    hash = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.uid'), nullable=False)
    redirect_uri = Column(String, nullable=True)

    # relazioni
    user = relationship("User", back_populates="documenti")


class OperatoreGruppo(Base):
    __tablename__ = "operatoregruppo"
    
    operator_id = Column(Integer, ForeignKey('operatori.uid', ondelete="CASCADE"), primary_key=True)
    group_id = Column(Integer, ForeignKey('gruppi.uid', ondelete="CASCADE"), primary_key=True)

    # relazioni
    operatore = relationship("Operatore", back_populates="gruppi")
    gruppo = relationship("Gruppo", back_populates="operatori")
