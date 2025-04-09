import os

API_ID = os.environ.get("API_ID", "23298276")

API_HASH = os.environ.get("API_HASH", "0fa5ea46f81eb24548cfc66b5d0f6107")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "8098279575:AAGAMKgRgSW4b0TvbE6njoYtpntTCiONw3E")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 6882767118))

LOG = -1002340573597,

# UPDATE_GRP = , # bot sat group

# auth_chats = []

try:
    ADMINS=[6882767118]
    for x in (os.environ.get("ADMINS", "6882767118").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)
