import json
import os

class Database:
    def insert(self, name, email, password):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        filename = os.path.join(BASE_DIR, 'users.json')
        
        # print("Reading from:", filename)

        # Read existing users
        with open(filename, 'r') as rf:
            users = json.load(rf)

        # Append new user   
        if email in users:
            print("User already exists.")
            return {"status": "error", "message": "User already exists."}
        else:
            users[email] = [name, password]

        # Write updated list
        with open(filename, 'w') as wf:
            json.dump(users, wf, indent=4)

        print("User successfully added.")
        return {"status": "success"}

    def search(self, email, password):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        filename = os.path.join(BASE_DIR, 'users.json')
        
        # Read existing users
        with open(filename, 'r') as rf:
            users = json.load(rf)

        if email in users:
            if users[email][1] == password:
                print("Login successful.")
                return {"status": "success", "name": users[email][0]}
            else:
                print("Incorrect password.")
                return {"status": "error", "message": "Incorrect password."}
        else:
            print("User not found.")
            return {"status": "error", "message": "User not found."}
