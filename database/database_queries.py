import datetime

from pydapper import connect
from database.connection_string import connection_string
from models.user_models import User


def fetch_user_by_email(email: str) -> int:
    with connect(connection_string) as commands:
        user_id_dict = commands.query_single(
            "select user_id from users where email = ?email?", param={"email": email})
        return user_id_dict["user_id"]


def insert_user(registration_details: User):
    with connect(connection_string) as commands:
        commands.execute("insert into users(first_name, last_name, phone, email, token, created_at, updated_at) "
                         "values(?first_name?, ?last_name?, ?phone?, ?email?, ?token?, ?created_at?, ?updated_at?)",
                         param={"first_name": registration_details.first_name, "last_name":
                                registration_details.last_name, "phone": registration_details.phone,
                                "email": registration_details.email, "token": registration_details.token,
                                "created_at": registration_details.created_at, "updated_at":
                                    registration_details.updated_at})


def user_exists(email: str) -> bool:
    with connect(connection_string) as commands:
        token = commands.query(
            "select token from users where email = ?email?", param={"email": email})

        print(token)
        if token == []:
            return False
        return True


def fetch_referral_code(email: str) -> str:
    if user_exists(email):
        with connect(connection_string) as commands:
            referral_code = commands.query_single(
                "select referral_code from Users inner join Referrals on Users.user_id= referrals.user_id where email "
                "= ?email?",
                param={"email": email})
        return referral_code["referral_code"]


def store_referral_code(referral_code, user_id: int):
    with connect(connection_string) as commands:
        commands.execute(
            "insert into Referrals ( referral_code, created_at, user_id, is_active) values(?referral_code?, "
            "?created_at?, ?user_id?, ?is_active?)",
            param={"referral_code": referral_code, "created_at": datetime.datetime.now(), "user_id": user_id,
                   "is_active": True})


def inactivate_referral_token(code):
    with connect(connection_string) as commands:
        commands.execute(
            "update Referrals set is_active = ?is_active? where referral_code = ?referral_code?",
            param={"is_active": False, "referral_code": code})


def delete_referral_token(code):
    with connect(connection_string) as commands:
        commands.execute(
            "delete from Referrals where referral_code = ?referral_code?",
            param={"referral_code": code})
