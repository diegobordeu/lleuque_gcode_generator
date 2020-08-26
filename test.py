import subprocess

snap_process=subprocess.Popen(["snapshot"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
output, errors= snap_process.communicate(input="q")
#snap_process.wait()
print(output)
print(errors)
