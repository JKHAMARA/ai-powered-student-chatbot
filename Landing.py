import streamlit as st
from auth import is_authenticated
from utils import hide_default_sidebar_navigation, chatbot_header, chat_bubble

# Hide default nav
hide_default_sidebar_navigation()

# Redirect logged-in users straight to chatbot
if is_authenticated():
    st.switch_page("pages/2_Chatbot.py")

# Initialize guest message counter
if "guest_messages" not in st.session_state:
    st.session_state["guest_messages"] = 0

# Header
chatbot_header()

st.info("You are currently using Guest Mode. You can only send **2 messages**. Please log in or register for unlimited access.")

# Chat display
st.write("### Chatbot")
chat_container = st.container()

# Simple input form
with st.form("guest_chat_form", clear_on_submit=True):
    user_input = st.text_input("Type your message here...")
    submitted = st.form_submit_button("Send")

if submitted and user_input:
    if st.session_state["guest_messages"] < 2:
        with chat_container:
            chat_bubble(user_input, is_user=True)
            chat_bubble("(Bot placeholder response)", is_user=False)
        st.session_state["guest_messages"] += 1
    else:
        st.warning("⚠️ You’ve reached the guest limit. Please log in or register to continue.")

# Sidebar (Landing only)
with st.sidebar:
    st.markdown("### Navigation")
    st.page_link("pages/1_Login_Register.py", label="Login / Register")
