# In a real-world app, this would be a database model with hashed passwords.
users_db = {
    "user1": {
        "username": "user1",
        "hashed_password": b"$2b$12$fGlYyoiUXmbFotlLR3gHpOStjqRKupuxXfHpzzCNZ8QeqJDqGIA.O" # password123
    },
    "user2": {
        "username": "user2",
        "hashed_password": b"$2b$12$vDTxDO9ji7jCmNVQAIKjyu2FhN4SSlPmlEpiqc/OQmzQ7FYfvPYcS" # password456
    }
}

# Functions to simulate password verification (passlib is used for bcrypt)
# from passlib.context import CryptContext
# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

import bcrypt

def verify_password(plain_password, hashed_password):
    password_byte_enc = plain_password.encode('utf-8')
    return bcrypt.checkpw(password = password_byte_enc , hashed_password = hashed_password)

def get_user(username: str):
    return users_db.get(username)
