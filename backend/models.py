from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from pygres.database import Base

class User(Base):
    __tablename__ = "User"

    UID = Column(Integer, primary_key=True, index=True)
    Username = Column(String(255), unique=True, nullable=False)
    PasswordHash = Column(Text, nullable=False)

    practices = relationship("Pratica", back_populates="user")
    documents = relationship("Documento", back_populates="user")


class Operatori(Base):
    __tablename__ = "Operatori"

    UID = Column(Integer, primary_key=True, index=True)
    Username = Column(String(255), unique=True, nullable=False)
    PasswordHash = Column(Text, nullable=False)


class Gruppi(Base):
    __tablename__ = "Gruppi"

    UID = Column(Integer, primary_key=True, index=True)
    GroupName = Column(String(255), nullable=False)
    ParentGroupID = Column(Integer, ForeignKey("Gruppi.UID"), nullable=True)

    parent = relationship("Gruppi", remote_side=[UID])


class Pratica(Base):
    __tablename__ = "Pratica"

    PracticeID = Column(Integer, primary_key=True, index=True)
    WalletAddress = Column(String(255), nullable=False)
    UserID = Column(Integer, ForeignKey("User.UID"), nullable=False)

    user = relationship("User", back_populates="practices")


class Documento(Base):
    __tablename__ = "Documento"

    DocID = Column(Integer, primary_key=True, index=True)
    Hash = Column(Text, nullable=False)
    UserID = Column(Integer, ForeignKey("User.UID"), nullable=False)
    RedirectURI = Column(Text, nullable=True)

    user = relationship("User", back_populates="documents")


class OperatoreGruppo(Base):
    __tablename__ = "OperatoreGruppo"

    OperatorID = Column(Integer, ForeignKey("Operatori.UID"), primary_key=True)
    GroupID = Column(Integer, ForeignKey("Gruppi.UID"), primary_key=True)
