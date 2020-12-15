import os

import synapseclient

synapse_username = os.getenv("INPUT_SYNAPSE_USERNAME")
synapse_apikey = os.getenv("INPUT_SYNAPSE_PASSWORD")

syn = synapseclient.login(username=synapse_username,
                          apiKey=synapse_apikey,
                          rememberMe=True)
