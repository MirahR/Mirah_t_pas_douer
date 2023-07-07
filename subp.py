import subprocess

if __name__=='__main__':
    with open("output.txt", "w") as f:
    subprocess.check_call(["python", "file.py"], stdout=f)
