# fileexchange
Snippet to exchange files

## to encode files 
```
python encode.py filename [OPTIONAL: code_bin.txt]
```

## To Split file into parts of 10 mega bytes 
```
cd /path/to/parts
split -b 10m ../filename
```

## To merge parts into filename
```
cat /path/to/parts/x* > filename
```

## to decode files
```
python code_bin.txt
```
