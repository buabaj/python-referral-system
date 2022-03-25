from fastapi import APIRouter, HTTPException
from models.user_models import User
from services.referral_system import referral_code_handler
from database.database_queries import user_exists, insert_user, fetch_user_by_email


router = APIRouter()


@router.post("/register_user")
async def register_user(user_details: User):
    if user_exists(user_details.email):
        raise HTTPException(status_code=400, detail="User already exists")
    else:
        insert_user(user_details)
        referral_code_handler(fetch_user_by_email(user_details.email))
        return {"message": "User registered successfully"}
