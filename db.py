import json
from pathlib import Path

DB_FILE = Path("users.json")

def init_db():
    if not DB_FILE.exists():
        with open(DB_FILE, "w") as f:
            json.dump({"users": []}, f)

def load_users():
    with open(DB_FILE, "r") as f:
        return json.load(f)["users"]

def save_user(user):
    data = {"users": load_users()}
    data["users"].append(user)
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=4)
