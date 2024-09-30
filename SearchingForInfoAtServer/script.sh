#! /bin/bash

# Look for files
find / -type f \( -name file1 -o -name file2 -o -name file3 -name file4 -name file5 \) 2>/dev/null
# More info about every found file
find / -type f \( -name file1 -o -name file2 -o -name file3 -name file4 -name file5 \) -exec ls -l {} 2>/dev/null 

