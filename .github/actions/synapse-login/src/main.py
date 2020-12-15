import os

import synapseclient

username = os.getenv("INPUT_USERNAME")
password = os.getenv("INPUT_PASSWORD")

syn = synapseclient.login(email=username,
                          password=password,
                          rememberMe=True)
