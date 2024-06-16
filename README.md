# fileexchange
Snippet to exchange files and related stuff.

Bash commands: 
## Encode files 
```
python encode.py filename [OPTIONAL: code_bin.txt]
```

## Split file into parts of 10 mega bytes 
```
cd /path/to/parts
split -b 10m ../filename
```

## To merge parts into filename
```
cat /path/to/parts/x* > filename
```

## To decode files
```
python code_bin.txt
```
