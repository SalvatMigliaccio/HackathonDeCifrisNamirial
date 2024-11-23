from fastapi import FastAPI, HTTPException
import uvicorn
from chain_utils import ChainUtils as cu
from models import SignRequest
from ring_signature import Ring as rs


app = FastAPI()


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


@app.get("/dossier/{dossier_address}", response_model=list[str])
def read_dossier(dossier_address):
    try:
        return cu.get_txs(dossier_address)
    except Exception as e:
        raise e


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True)