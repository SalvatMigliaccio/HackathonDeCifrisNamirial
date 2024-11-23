import logging
from typing import Any

from fastapi import APIRouter, Depends, Request
from pydantic.networks import EmailStr

from backend import models, schemas
from backend.endpoints import deps
from backend.core.utils import send_test_email


router = APIRouter()

logger = logging.getLogger(__name__)


@router.post("/test-email/", response_model=schemas.Msg, status_code=201)
def test_email(
    email_to: EmailStr,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Test emails.
    """
    send_test_email(email_to=email_to)
    return {"msg": "Test email sent"}


@router.get('/status')
def status():
    return {'api': 'Ok'}
