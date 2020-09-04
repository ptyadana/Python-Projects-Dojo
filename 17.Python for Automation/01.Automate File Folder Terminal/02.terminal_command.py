import subprocess

for i in range(5):
    # call another script
    subprocess.check_call(['python', 'hello_world.py'])
