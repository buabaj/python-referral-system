# python-referral-system

A referral system built using FastAPI and SQLite3. This system allows users to generate referral codes, check status of referral codes, redeem referral codes and invalidate codes after a set stale period.

# Features

- [x] Built-in Referral Code Expiry
- [x] Generate referral code
- [x] Check validity of referral Code
- [x] Redeem referral code
- [x] Strong types and type enforcing

# Core Requirements

- FastAPI
- SQLite3

# Project Setup

1. Make sure you have SQLite3 installed on your machine. Next, Clone this repo and navigate to the root directory.

```bash
git clone git@github.com:buabaj/python-referral-system.git
cd python-referral-system
```

2. Create and activate a virtual environment for the requirements of your project.

```bash
python3 -m venv .venv/
source .venv/bin/activate
pip install -r requirements.txt
```

3. Start your sqlite3 server in your terminal using the command:
   
```bash
sqlite3 test.db
```

4. Paste the following SQL command in the sqlite3 prompt that comes on in your terminal to create your database tables:
   
```SQL
CREATE TABLE Users(
    user_id INTEGER PRIMARY KEY AutoIncrement,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    phone TEXT,
    email TEXT NOT NULL,
    token TEXT,
    created_at DATE,
    updated_at DATE
);

CREATE TABLE Referrals(
    referral_code_id INTEGER PRIMARY KEY AutoIncrement,
    referral_code TEXT NOT NULL,
    created_at DATE,
    is_active boolean NOT NULL,
    user_id INT NOT NULL,
    foreign key(user_id) references Users(user_id)

);
```

5. Run the following code in a different terminal to run your local FastAPI server:

```bash
python3 app.py
```

6. Head to `localhost:8000/docs` in your browser to test the Implementation of the referral system endpoints and documentation in an interactive SWAGGER UI API Documentation playground.

