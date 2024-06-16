# code to encode contents of filepath in a binary 
import sys

if len(sys.argv) < 2:
    raise TypeError('Missing arguments filepath and [(OPTIONAL) output_code_filepath]')

filepath = sys.argv[1]

f = open(filepath, "rb")
binary_content = f.read()
f.close()

import os
filename = (os.path.basename(filepath))

code = f"""
x = {str(binary_content)}
f = open(\"{filename}\", "wb")
f.write(x)
f.close()
"""

if len(sys.argv) < 3:
    outfilepath = 'code_bin.txt'
else:
    outfilepath = sys.argv[2]

f = open(outfilepath, "w")
f.write(code)
f.close()
