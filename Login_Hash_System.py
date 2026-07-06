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

    print("\nAccount created successfully :)")

# _________________________________________________________________________________________________

def login():

    print("\n=== Login ===")

    username = input("Username : ")
    password = input("Password : ")

    password_hash = hash_password(password)

    if not os.path.exists(FILE_NAME):
        print("\nNo users have been registered :(")
        return

    with open(FILE_NAME, "r") as file:

        for line in file:

            saved_username, saved_hash = line.strip().split(":")

            if username == saved_username and password_hash == saved_hash:
                print("\nLogin Successful :)")
                return

    print("\nInvalid username or password :(")

# _________________________________________________________________________________________________

while True:

    print('''
====================
=== Login System ===
====================

1. Create Account
2. Login
3. Exit
''')

    choice = input("Choose an option: ")

    if choice == "1":
        CreateAccount()

    elif choice == "2":
        login()

    elif choice == "3":
        print("\nGoodbye")
        break

    else:
        print("\nInvalid choice")
        
# _________________________________________________________________________________________________