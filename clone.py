#!/usr/bin/env python3

import subprocess as sub
import os


pat: str = ""  #put your PAT here
usr: str = "AJIyanu"
repo: str = input("enter repo_name:\n")
resp: str = "d"

print("\n\n************************************************************\n\n")
resp = input("Enter username  or type 'd' to use default: ")
if resp != "d":
    usr = resp
url = "https://{}@github.com/{}/{}.git".format(pat, usr, repo)
sub.call(["git", "clone", url])

print("\n\n************************************************************\n\n")
resp = input("Would you like a README in the repo? 'Y' to yes/'R' to exit /anykey to skip: ")
if resp == "R":
    exit()
if resp == "Y":
    lines = []
    print("Type each line and then Enter")
    print("enter 'done' when done otherwise you are stuck in endless loop")
    print("don't worry 'done' won't be appended")
    while resp != "done":
        resp = input("")
        lines.append(resp)
    path: str = f"{repo}/README.md"
    lines.pop()
    with open(path, 'w') as file:
        file.writelines(line + '\n' for line in lines)
else:
    print("skipped")


print("\n\n************************************************************\n\n")
os.chdir(repo)
reply: str = input("would you like to create directory in the repo?:('Y' creates, 'R' exits anykey to skip) ")
if resp == 'R':
    exit()
if resp == 'Y':
    folder = input("Enter directory name: ")
    try:
        sub.call(["mkdir", folder])
    except Exception as e:
        print("exiting because", e)
        exit()
    lines = []
    print("\n\n************************************************************\n\n")
    print("Enter the content of the readme, please type the word 'done' when done otherwise locked in emdless loop")
    while resp != "done":
        resp = input("")
        lines.append(resp)
    path = "{}/README.md".format(folder)
    with open(path, 'w') as file:
        file.writelines(line + '\n' for line in lines)
cmd = "git add .".split()
sub.call(cmd)
cmd = "git commit -m clone".split()
sub.call(cmd)
cmd = "git push".split()
sub.call(cmd)
