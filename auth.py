import streamlit as st
import json
import os
from db import load_users, save_user, init_db

SESSION_FILE = "session.json"
init_db()

def register_user(username, password, department):
    users = load_users()
    if any(u["username"] == username for u in users):
        return False, "Username already exists."
    new_user = {"username": username, "password": password, "department": department}
    save_user(new_user)
    st.session_state["user"] = new_user
    return True, "Registration successful."

def login_user(username, password):
    users = load_users()
    for u in users:
        if u["username"] == username and u["password"] == password:
            st.session_state["user"] = u
            return True
    return False

def logout_user():
    if "user" in st.session_state:
        del st.session_state["user"]
    st.session_state["guest_messages"] = 0  # reset guest counter
    _clear_session()  # clear persistent session

def is_authenticated():
    # First check session_state
    if "user" in st.session_state:
        return True
    # Then check persistent session file
    user = _load_session()
    if user:
        st.session_state["user"] = user
        return True
    return False

# --- Internal helpers ---
def _save_session(user):
    with open(SESSION_FILE, "w") as f:
        json.dump(user, f)

def _load_session():
    if os.path.exists(SESSION_FILE):
        with open(SESSION_FILE, "r") as f:
            return json.load(f)
    return None

def _clear_session():
    if os.path.exists(SESSION_FILE):
        os.remove(SESSION_FILE)
