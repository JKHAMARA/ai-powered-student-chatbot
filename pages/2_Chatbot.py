import streamlit as st
from auth import is_authenticated
from utils import hide_default_sidebar_navigation, chatbot_header, chat_bubble, sidebar_profile

# Hide nav
hide_default_sidebar_navigation()

if not is_authenticated():
    st.switch_page("Landing.py")

# Header
chatbot_header()

# Sidebar = Profile + Logout (now from utils)
sidebar_profile()

# Main Chat Interface
chat_container = st.container()

with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("Type your message here...")
    submitted = st.form_submit_button("Send")

if submitted and user_input:
    with chat_container:
        chat_bubble(user_input, is_user=True)
        chat_bubble("(Bot placeholder response)", is_user=False)
