import os

import synapseclient

syn = synapseclient.login()

ent = syn.get(os.getenv("INPUT_SYNID"))

# Set the fact-output of the action as the value of random_fact
print(f"::set-output name=path::{ent.path}")