from pydantic import BaseModel, Field
from typing import Optional, List

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password_hash: str

class UserRead(UserBase):
    UID: int

    class Config:
        orm_mode = True


class OperatoriBase(BaseModel):
    username: str

class OperatoriCreate(OperatoriBase):
    password_hash: str

class OperatoriRead(OperatoriBase):
    UID: int

    class Config:
        orm_mode = True


class GruppiBase(BaseModel):
    GroupName: str
    ParentGroupID: Optional[int] = None

class GruppiRead(GruppiBase):
    UID: int

    class Config:
        orm_mode = True


class PraticaBase(BaseModel):
    WalletAddress: str
    UserID: int

class PraticaRead(PraticaBase):
    PracticeID: int

    class Config:
        orm_mode = True


class DocumentoBase(BaseModel):
    Hash: str
    UserID: int
    RedirectURI: Optional[str] = None

class DocumentoRead(DocumentoBase):
    DocID: int

    class Config:
        orm_mode = True


class OperatoreGruppoBase(BaseModel):
    OperatorID: int
    GroupID: int
