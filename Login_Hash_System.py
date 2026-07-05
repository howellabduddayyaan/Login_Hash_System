# =========================
# === Login Hash System ===
# =========================

import hashlib
import os

FILE_NAME = "users.txt"

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# _________________________________________________________________________________________________

def CreateAccount():

    print("\n=== Create Account ===")

    username = input("Username: ")
    password = input("Password: ")

    password_hash = hash_password(password)

    with open(FILE_NAME, "a") as file:
        file.write(f"{username}:{password_hash}\n")



# _________________________________________________________________________________________________