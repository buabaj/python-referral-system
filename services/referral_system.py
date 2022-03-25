from database.connection_string import connection_string
from pydapper import connect
import secrets
import threading

from database.database_queries import store_referral_code, inactivate_referral_token, delete_referral_token

stale_time = 60 * 60 * 24 * 2


def referral_code_handler(user_id: int):
    store_referral_code(generate_referral_code(), user_id)


def generate_referral_code() -> str:
    code = secrets.token_urlsafe(8)
    expire_referral_code(code)
    return code


def is_active_referral_code(code: str) -> bool:
    is_active_dict: int
    with connect(connection_string) as commands:
        is_active_dict = commands.query_single(
            "select is_active from Referrals where referral_code = ?referral_code?",
            param={"referral_code": code})

    if is_active_dict["is_active"]:
        return True
    else:
        return False


def redeem_referral(code: str):
    invalidate_referral_code(code)


def invalidate_referral_code(code: str):
    inactivate_referral_token(code)


def set_interval_for_code_invalidation(func, sec):
    def func_wrapper():
        set_interval_for_code_invalidation(func, sec)
        func()

    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t


def expire_referral_code(code: str):
    set_interval_for_code_invalidation(invalidate_referral_code, stale_time)
