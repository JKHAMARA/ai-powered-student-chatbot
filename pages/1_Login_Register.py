import streamlit as st
from auth import register_user, login_user, is_authenticated, _save_session
from utils import hide_default_sidebar_navigation, chatbot_header

st.set_page_config(page_title="Login/Register", layout="centered", initial_sidebar_state="collapsed")

# Hide nav + clear sidebar
hide_default_sidebar_navigation()
st.sidebar.empty()

if is_authenticated():
    st.switch_page("pages/2_Chatbot.py")

# Header
chatbot_header()

st.title("🔐 Login or Register")

tab1, tab2 = st.tabs(["Login", "Register"])

with tab1:
    username = st.text_input("Username", key="login_user")
    password = st.text_input("Password", type="password", key="login_pass")
    if st.button("Login"):
        if login_user(username, password):
            _save_session(st.session_state["user"])  # persist session
            st.success("Login successful! Redirecting...")
            st.switch_page("pages/2_Chatbot.py")
        else:
            st.error("Invalid credentials.")

with tab2:
    new_user = st.text_input("New Username")
    new_pass = st.text_input("New Password", type="password")
    dept = st.selectbox("Department", ["Computer Science"])
    if st.button("Register"):
        ok, msg = register_user(new_user, new_pass, dept)
        if ok:
            _save_session(st.session_state["user"])  # persist session
            st.success(msg)
            st.switch_page("pages/2_Chatbot.py")
        else:
            st.error(msg)

st.warning("⚠️ Guests can chat but are limited to **2 prompts** until they register.")
