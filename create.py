import sys
import os
from github import Github

lang = str(sys.argv[1])
path = f"F:\craigComp\Programming\{lang}"

username = "craiglobo1" #Insert your github username here
password = "Craig123$" #Insert your github password here

def create():
    folderName = str(sys.argv[2])
    os.makedirs(os.path.join(path,folderName))
    md = open(os.path.join(path,folderName) +r'\README.md','w')
    md.close()
    user = Github(username, password).get_user()
    repo = user.create_repo(folderName)
    print("Succesfully created repository {}".format(folderName))

if __name__ == "__main__":
    create()
