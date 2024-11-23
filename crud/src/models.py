from pydantic import BaseModel


class SignRequest(BaseModel):
    sign: list[int]
    entity_seed: str
    dossier_address: str
    document_uri: str
    group: int
