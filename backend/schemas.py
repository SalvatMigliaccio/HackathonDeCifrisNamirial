from pydantic import BaseModel, Field
from typing import Optional, List

class UserBase(BaseModel):
    Username: str

class UserCreate(UserBase):
    PasswordHash: str

class UserRead(UserBase):
    UID: int

    class Config:
        orm_mode = True


class OperatoriBase(BaseModel):
    Username: str

class OperatoriCreate(OperatoriBase):
    PasswordHash: str

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
