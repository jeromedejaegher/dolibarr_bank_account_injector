# dolibarr_bank_account_injector

# PURPOSE

WIP : streamlit app to securely inject bank statement.

This app will use dolibarr API.

# LICENCE

I use GNU Licence 3, which is the one used by dolibarr, to facilitate any integration.
If you use any of the components of this repo, just let me know and credit me as :

dolibarr_bank_account_injector, jerome dejaegher, 2026, https://github.com/jeromedejaegher/dolibarr_bank_account_injector

# INSTALL

First, install Dolibarr and get a Dolikey

Then, clone the repo : 

```bash
git clone https://github.com/jeromedejaegher/dolibarr_bank_account_injector.git
cd dolibarr_bank_account_injector
```

Create a .env file at the root of the project and fill it with the ip adress of your dolibarr server and your API key : 

```txt
# Dolibarr adress and secrets

"API_URL"=localhost # or 192.168.0.1 or ...
"DOLAPIKEY"=your_api_key
```

create venv and activate it :
```bash
uv venv
source .venv/bin/activate
```

install the package : 
```bash
uv pip install -e .
```

# Launch

Use .sh (Linux) or .bat (Windows) file.

run the app (linux): 
```bash
account_injector.sh
```

run the app (windows): 
```bash
account_injector.bat
```
