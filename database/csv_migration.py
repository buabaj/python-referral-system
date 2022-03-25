import csv
from pydapper import connect
from database.database_queries import fetch_user_by_email
from services.referral_system import referral_code_handler
from database.connection_string import connection_string

"""inserts list of users into database and calls referral_code_handler to generate referral codes"""


def insert_users_from_csv(csv_filename):
    with open(csv_filename, 'r') as csvfile:
        users = csv.DictReader(csvfile)

        for user in users:
            with connect(connection_string) as commands:
                commands.execute(
                    "insert into users(first_name, last_name,phone, email,token, created_at, updated_at ) values("
                    "?first_name?, ?last_name?, ?phone?, ?email?, ?token?, ?created_at?, ?updated_at?)",
                    param={"first_name": user["first_name"], "last_name": user["last_name"], "phone": user["phone"],
                           "email": user["email"], "token": user["token"], "created_at": user["created_at"],
                           "updated_at": user["updated_at "]})

            referral_code_handler(fetch_user_by_email(user["email"]))


insert_users_from_csv("dummy-data.csv")
