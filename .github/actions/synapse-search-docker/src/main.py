import os

import synapseclient

syn = synapseclient.login()

docker_repos = syn.getChildren(os.getenv("INPUT_PARENTID"),
                               includeTypes=['dockerrepo'])
submitted_docker_info = os.getenv("INPUT_DOCKER_REPO").split(":")

submitted_docker_repo = submitted_docker_info[0]
submitted_docker_tag = submitted_docker_info[1]

for docker_repo in docker_repos:
    docker_ent = syn.get(docker_repo['id'])
    if docker_ent.repositoryName == submitted_docker_repo:
        synid = docker_repo['id']
        break

# Set the fact-output of the action as the value of random_fact
print(f"::set-output name=synid::{synid}")
print(f"::set-output name=tag::{submitted_docker_tag}")