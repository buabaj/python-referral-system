from fastapi import APIRouter
from services.referral_system import redeem_referral


router = APIRouter()


@router.post("/redeem_referral_code")
def redeem_referral_code(referral_code: str):
    redeem_referral(referral_code)
    return {"message": "Referral code redeemed successfully"}
