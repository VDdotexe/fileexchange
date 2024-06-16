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

## Merge parts into filename
```
cat /path/to/parts/x* > filename
```

## Decode file
```
python code_bin.txt
```
