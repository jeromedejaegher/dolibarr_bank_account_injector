from loguru import logger
import streamlit as st
import pandas as pd

# load api key from .env as hidden_state


st.title("Dolibar account injector")

uploaded_file = st.file_uploader(
    label="load account statement in excel format", 
    type="xlsx", accept_multiple_files=False, 
    width="stretch")

if uploaded_file:

    # 3 boutons : reset, upload

    dataframe = pd.read_excel(uploaded_file)
    st.write(dataframe)
    logger.info(f"uploaded_file")
