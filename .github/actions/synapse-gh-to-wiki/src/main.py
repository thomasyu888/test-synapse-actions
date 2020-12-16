import os

import synapseclient

syn = synapseclient.login()
synid = os.getenv("INPUT_SYNID")

wiki_content = ""
if os.path.exists("README.md"):
    wiki_content += "# Description\n\n"
    with open("README.md") as readme_f:
        wiki_content += readme_f.read()

if os.path.exists("Dockerfile"):
    wiki_content += "\n\n"
    wiki_content += "# Dockerfile\n\n"
    with open("Dockerfile") as readme_f:
        wiki_content += readme_f.read()

wiki = synapseclient.Wiki(owner=synid, markdown=wiki_content)
syn.store(wiki)
