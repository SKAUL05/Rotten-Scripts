import subprocess
subprocess.getoutput('git add .')
message = input("Enter commit message")
subprocess.getoutput(f'git commit -m {message}')
branchname = input("Enter branch name")
subprocess.getoutput(f'git push origin {branchname}')