from fastapi import APIRouter, Depends, HTTPException, Form
from sqlalchemy.orm import Session
from pydantic import BaseModel
from endpoints.deps import get_db, get_current_active_user
import models, crud

router = APIRouter()



@router.post("/link_dossier")
async def link_dossier(
    *,
    db: Session = Depends(get_db),
    dossier_address: str = Form(...),
    current_user: models.User = Depends(get_current_active_user)
):
    """
    Link a dossier to a user.
    """
    
    dossier = await crud.get_pratica_by_wallet_address(db, address=dossier_address)
    if not dossier:
        raise HTTPException(status_code=404, detail="Dossier not found")
    
    await crud.create_pratica(db, user_id=current_user.id, dossier_id=dossier_address)
    return {"message": "Dossier linked to user successfully"}