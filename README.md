# KutilsDiscordBot


## Developer Setup
Requirements: Python 3.7+

1. Optionally, create a virtual environment by running `python3 -m venv .venv` and activate it according to your OS
2. Run `python3 -m pip install -r requirements.txt`
3. Create a `.env` file at the root. Populate it as follows:
```
MONGO_CONN=your_mongo_connection
DISC_TOKEN=your_discord_token
GOOGLE_CRED_JSON=path_to_google_service_account_credentials
```
4. Run the Discord Bot using `python3 kutilsbot.py`

We utilize logging heavily - please configure the logging level for your application 

## Install on your Discord Server
Soon!

## Architecture
