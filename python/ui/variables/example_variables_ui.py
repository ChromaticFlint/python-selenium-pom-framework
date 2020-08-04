#!/usr/bin/python3
"""
This file stores the global variables. Change them here to modify tests.
NOTE: Eventually, this file should not be added to git. Each person should have
    their own local instance of this file, with their own credentials. Fine for
    now, to be included with repo. You will want to rename this to "variables_ui.py"
    after adding in the correct username and password below.

TODO: Change this to be argument based, with defaults.
# TARGETS
# CHANGE THIS TO CHANGE:
#   - BASE_URL
#   - BASE_USERNAME
#   - BASE_PASSWORD
"""
TARGET = 0

# Credentials and Environments
PROD = ["UserName", "Password"]
UAT = ["UserName", "Password"]
BASE = {
    0: ["https://www.google.com/#this-is-an-example", PROD[0], PROD[1]],
    1: ["", UAT[0], UAT[1]],
}


# Finalized Credentials and Environments
BASE_URL = BASE[TARGET][0]
BASE_USERNAME = BASE[TARGET][1]
BASE_PASSWORD = BASE[TARGET][2]
