import streamlit as st

def chatbot_header():
    st.markdown(
        """
        <h2 style="text-align:center; font-family: 'Segoe UI', sans-serif; color:#003366;">
            STUDENT ASSISTANT CHATBOT
        </h2>
        """,
        unsafe_allow_html=True,
    )

def chat_bubble(message, is_user=False):
    if is_user:
        st.markdown(
            f"""
            <div style="text-align:right; margin:5px;">
                <span style="background:#003366; color:white; padding:8px 12px; border-radius:12px; font-family: 'Segoe UI';">
                    {message}
                </span>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.markdown(
            f"""
            <div style="text-align:left; margin:5px;">
                <span style="background:#F1F1F1; padding:8px 12px; border-radius:12px; font-family: 'Segoe UI';">
                    {message}
                </span>
            </div>
            """, unsafe_allow_html=True)

def sidebar_profile():
    user = st.session_state.get("user", {})
    st.sidebar.image(
        "https://www.svgrepo.com/show/382103/avatar.svg", width=80
    )
    st.sidebar.write(f"**{user.get('username', 'Guest')}**")
    st.sidebar.write(f"Department: {user.get('department', 'N/A')}")
    if st.sidebar.button("Logout"):
        from auth import logout_user
        logout_user()
        st.sidebar.success("Logged out successfully")

def hide_default_sidebar_navigation():
    """Hide Streamlit's default multipage sidebar navigation."""
    hide_pages_style = """
        <style>
            [data-testid="stSidebarNav"] {display: none;}
        </style>
    """
    st.markdown(hide_pages_style, unsafe_allow_html=True)