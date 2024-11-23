from fastapi import FastAPI
import uvicorn
from chain_utils import ChainUtils as cu

app = FastAPI()


# sign document
@app.post("/sign")
def upload_sign(
    sign: list[int],
    entity_seed: str,
    dossier_address: str,
):
    memos = [cu.parse_memo(hex(s)) for s in sign]
    cu.send_transaction(entity_seed, dossier_address, memos)


@app.get("/dossier")
def read_dossier(dossier_address):
    return cu.get_txs(dossier_address)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True)
