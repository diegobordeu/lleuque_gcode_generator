import subprocess
import datetime
import sys
import time
import os

day = sys.argv[2]
hour = sys.argv[4]

subprocess.run(["mkdir", "-p", f"./image_storage/{day}/{hour}"])
os.chdir(f"./image_storage/{day}/{hour}/")
# subprocess.run("ls")
subprocess.run(['python3','../../../snapshot.py','--oneshot'])

