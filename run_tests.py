import os
import subprocess

path = "/media/sf_Shared_folder/EC530"
for myfile in os.listdir(path):
    if myfile.endswith(".py") and myfile[0] == 'm':
        print("Linting " + myfile)
        subprocess.run(["autopep8", "--in-place", "-a", "-a", myfile])
        subprocess.run(["flake8", myfile])

print("Running Unit Tests: ")
for myfile in os.listdir(path):
    if myfile.endswith("tester.py") and myfile[0] == 'm':
        subprocess.run(["pytest", myfile])
