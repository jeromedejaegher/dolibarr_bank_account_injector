from loguru import logger
import streamlit as st
import requests, json
import pandas as pd

# load api key from .env as hidden_state
from dotenv import load_dotenv

import os

def get_header(apikey:str | None) -> dict:
    return {
            'DOLAPIKEY': apikey,
            'Content-Type': 'application/json'
        }

def get_all_accounts(dolibarr_url : str, apikey : str):
    headers = get_header(apikey=apikey)

    api_adress = f"http://{dolibarr_url}/api/index.php/bankaccounts?sortfield=t.rowid&sortorder=ASC&limit=100&page=1"
    api_adress = f"http://{dolibarr_url}/api/index.php/bankaccounts"

    # Make a get request with the parameters.
    clean_response = requests.get(url=api_adress, headers=headers)

    clean_response = clean_response.json()

    accounts_list = {elem["id"]: elem["ref"] for elem in clean_response}

    logger.info(accounts_list)

    return accounts_list

def get_all_lines(account: str, dolibarr_url : str, apikey : str):

    headers = get_header(apikey=apikey)
    api_adress = f"http://{dolibarr_url}/api/index.php/bankaccounts/{account}/lines"

    # Make a get request with the parameters.
    response = requests.get(url=api_adress, headers=headers)

    # Print the content of the response
    all_lines = response.json()

    lines_list = [{key: elem[key] for key in elem if elem[key]} for elem in all_lines]

    logger.info(f"all_lines : {lines_list}")

    return lines_list

load_dotenv()  # Loads .env file into os.environ

st.session_state["api_url"] = os.getenv("API_URL", None)
st.session_state["secret_key"] = os.getenv("DOLAPIKEY", None)

if not st.session_state.secret_key:
    msg = "API Key is missing, please configure you .env file at the root of the project"
    logger.info(msg)
    st.info(msg, icon="ℹ️")

logger.info(f"session_state : {st.session_state}")

st.title("Dolibar account injector")

all_bank_accounts = get_all_accounts(
    dolibarr_url=st.session_state["api_url"], 
    apikey=st.session_state["secret_key"]
)


    # Print the content of the response
logger.info(f"all_bank_accounts : {all_bank_accounts}")

bank_account = st.selectbox("Choose a  bank account", [all_bank_accounts[elem] for elem in all_bank_accounts])
bank_account_id = int([elem for elem in all_bank_accounts if all_bank_accounts[elem]==bank_account][0])

logger.info(f"choosen bank_account : {bank_account_id} - {bank_account}")

uploaded_file = st.file_uploader(
    label="load account statement in excel format", 
    type="xlsx", accept_multiple_files=False, 
    width="stretch")

if uploaded_file:

    # 3 boutons : reset, upload

    dataframe = pd.read_excel(uploaded_file)
    st.write(dataframe)
    logger.info(f"uploaded_file")

col1, col2, col3 = st.columns(3)

col1.button(label="get all lines", on_click=get_all_lines, 
                        args=[bank_account_id, st.session_state["api_url"], st.session_state["secret_key"]])
