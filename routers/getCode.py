from fastapi import APIRouter
from database.database_queries import fetch_referral_code


router = APIRouter()


@router.post("/get_referral_code")
async def get_referral_code(email: str):
    return fetch_referral_code(email)
