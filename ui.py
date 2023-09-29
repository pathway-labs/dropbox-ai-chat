import os
import json
import shutil
import pandas as pd
import streamlit as st
import requests
from dotenv import load_dotenv
from enum import Enum
import time

# Load environment variables
load_dotenv()
api_host = os.environ.get("HOST", "0.0.0.0")
api_port = int(os.environ.get("PORT", 8080))


# Streamlit UI elements
st.title("Dropbox Search Tool")

question = st.text_input(
    "Search for something",
    placeholder="What data are looking for?"
)


if question:
    url = f'http://{api_host}:{api_port}/'
    data = {"query": question}

    response = requests.post(url, json=data)

    if response.status_code == 200:
        st.write("### Answer")
        st.write(response.json())
    else:
        st.error(f"Failed to send data to Pathway API. Status code: {response.status_code}")
