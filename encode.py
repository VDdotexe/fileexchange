# code to encode contents of filename in a binary 
import sys

if len(sys.argv) < 2:
    raise TypeError('Missing arguments filename and [(OPTIONAL) output_code_filename]')

filename = sys.argv[1]

f = open(filename, "rb")
binary_content = f.read()
f.close()

code = f"""
x = {str(binary_content)}
f = open(\"{filename}\", "wb")
f.write(x)
f.close()
"""

if len(sys.argv) < 3:
    outFilename = 'code_bin.txt'
else:
    outFilename = sys.argv[2]

f = open(outFilename, "w")
f.write(code)
f.close()
