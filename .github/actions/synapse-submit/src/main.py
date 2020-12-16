import os

import synapseclient

syn = synapseclient.login()
queueid = os.getenv("INPUT_EVALUATIONID")
synid = os.getenv("INPUT_SYNID")
teamid = os.getenv("INPUT_TEAMID")
dockertag = os.getenv("INPUT_DOCKERTAG")

submission = syn.submit(queueid, synid, team=teamid, dockerTag=dockertag)

# Set the submission id
print(f"::set-output name=submissionid::{submission['id']}")