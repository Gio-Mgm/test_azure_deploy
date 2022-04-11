import requests
import streamlit as st

# streamlit settings
st.set_page_config(
    page_title='Azure_deploy',
    page_icon='	:spock-hand:',
    layout='centered',
    initial_sidebar_state='expanded'
)

# state session config
state = st.session_state
# if 'user' not in state:
#     state.user = None
# if 'user_id' not in state:
#     state.user_id = ""

API_PATH = 'http://127.0.0.1:8000'

r = requests.get(API_PATH)
if r.status_code == 200:
    st.title(r.json()['message'])
