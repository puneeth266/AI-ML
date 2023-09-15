# command.py

import subprocess
import sys

if len(sys.argv) != 2:
    print("Usage: python command.py <filename>")
    #sys.exit(1)

filename = sys.argv[1]

try:
    result = subprocess.check_output(["python", "wordcount.py", filename])
    print(result.decode())
except subprocess.CalledProcessError as e:
    print(f"Error: {e}")
