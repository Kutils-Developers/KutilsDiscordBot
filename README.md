# KutilsDiscordBot
A Discord Bot that reports dead hyperlinks on a Google Sheet for services like YouTube and Twitter. "Dead" links include when a YouTube video is made private and when Twitter accounts are inactive past a certain month threshold.

This project is an implementation of the original script-bank [mech-a/Kutils](https://github.com/mech-a/Kutils) to be a highly-integratable service for K-pop communities.

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
We follow a [MVC](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller) design pattern throughout our code. Our view is the Discord Bot that can be found in `kutilsbot.py` which uses abstracted components called cogs in the `cogs/` folder. Our controller is the `api/__init__.py` file which defines our objects and persists individual instances of the bot running on different servers. The model is the `api/models/__init__.py` file which contains the architecture of the program.
