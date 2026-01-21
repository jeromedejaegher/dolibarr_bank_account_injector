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
