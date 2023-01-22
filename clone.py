#!/usr/bin/env python3

import subprocess as sub
import os


pat = "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"
usr = "AJIyanu"
repo: str = input("enter repo_name:\n")
resp = "d"

resp = input("Enter username  or type 'd' to use default: ")
if resp != "d":
    usr = resp
url = "https://{}@github.com/{}/{}.git".format(pat, usr, repo)
sub.call(["git", "clone", url])

resp = input("Would you like a README in the repo? 'Y' to yes/'R' to exit /anykey to skip: ")
if resp == "R":
    exit()
elif resp == "Y":
    lines = []
    print("Enter the content of the readme, please type the word 'done' when done otherwise locked in emdless loop")
    while resp != "done":
        resp = input("")
        lines.append(resp)
    path = "{}/README.md".format(repo)
    with open(path, 'w') as file:
        file.writelines(line + '\n' for line in lines)
else:
    print("skipped")


os.chdir(repo)
resp = input("would you like to create directory in the repo?: ('Y' creates, 'R' exits anykey to skip) ")
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