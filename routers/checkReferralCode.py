from fastapi import APIRouter, HTTPException
from services.referral_system import is_active_referral_code


router = APIRouter()


@router.post("/check_referral_code_validity")
async def check_referral_code_validity(referral_code: str):
    try:
        return is_active_referral_code(referral_code)
    except Exception:
        raise HTTPException(
            status_code=400, detail="Referral code is not valid")
