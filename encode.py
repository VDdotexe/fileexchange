# code to encode contents of filename in a binary 

filename = "20240502_171538.jpg"

f = open(filename, "rb")
binary_content = f.read()
f.close()

code = f"""
x = {str(binary_content)}
f = open(\"{filename}\", "wb")
f.write(x)
f.close()
"""

f = open("code.txt", "w")
f.write(code)
f.close()