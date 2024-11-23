from fastapi import FastAPI, HTTPException
import uvicorn
from chain_utils import ChainUtils as cu
from models import DossierResponse, SignRequest
from ring_signature import Ring as rs
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()
origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:3000",
    "http://localhost:8001"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/sign")
def upload_sign(sign_request: SignRequest):
    g = get_group_by_id(sign_request.group)
    ring = rs(g)
    verification = ring.verify_message(sign_request.document_uri, sign_request.sign)
    if not verification:
        raise HTTPException(status_code=401)

    memos = [cu.parse_memo(hex(s)) for s in sign_request.sign]
    tx = cu.send_transaction(
        sign_request.entity_seed, sign_request.dossier_address, memos
    )
    return tx.to_dict.get("hash")


@app.post("/dossier", response_model=DossierResponse)
def create_dossier():
    account = cu.create_account()
    return account


@app.get("/dossier/{dossier_address}", response_model=list[str])
def read_dossier(dossier_address):
    try:
        return cu.get_txs(dossier_address)
    except Exception as e:
        raise e


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
