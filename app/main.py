import streamlit as st
import os
import sys

#from ..db.database  import init_db

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

sys.path.append(BASE_DIR)

from db.database import init_db

init_db()
st.set_page_config(page_title="DocManager", layout="wide")

st.title("Smart PDF Document Manager")

st.divider()

tabs = st.tabs(["Upload", "Search & View", "Analytics"])

with tabs[0]:
    # Logic for upload
    pass

with tabs[1]:
    pass

with tabs[2]:
    pass