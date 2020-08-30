import subprocess

p1=subprocess.run(["snapshot"], capture_output=True, text=True)
p2=subprocess.run([" "], input=p1.stdout)

