import subprocess
import datetime
import sys

print(sys.argv)
day = sys.argv[2]
hour = sys.argv[4]

x = datetime.datetime.now()
print(x)

subprocess.run("mkdir", "-p", f"./image_storage/{day}/{hour}")
subprocess.run("cd", f"./image_storage/{day}/{hour}")
subprocess.run(['python3','../../snapshot.py','--oneshot'])

