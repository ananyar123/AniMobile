import json

USER_DATA_FILE = "userDatabase.json"

def load_users():
    try:
        with open(USER_DATA_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_users(users):
    with open(USER_DATA_FILE, "w") as file:
        json.dump(users, file)

def returningUser():
    users = load_users()
    
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    if username in users and users[username] == password:
        print("Welcome, " + username + "!")
    else:
        print("Not recognized. Please try again or create an account.")

def createUser():
    users = load_users()
    
    username = input("Create your username: ")
    if username in users:
        print("Username in use.")
        return
    
    password = input("Set your password: ")
    confirm_password = input("Confirm password: ")

    if password == confirm_password:
        users[username] = password
        save_users(users)
        print("Account created.")
    else:
        print("Passwords must match.")

if __name__ == "__main__":
    choice = input("Do you want to sign into an existing account? (yes/no): ").strip().lower()
    if choice == "yes":
        returningUser()
    elif choice == "no":
        createUser()
    else:
        print("Error...")
   
