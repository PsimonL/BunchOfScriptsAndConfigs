#! /bin/bash

# Based on https://tryhackme.com/r/room/ninjaskills

# Look for files
find / -type f \( -name file1 -o -name file2 -o -name file3 -name file4 -name file5 \) 2>/dev/null
# More info about every found file
find / -type f \( -name file1 -o -name file2 -o -name file3 -name file4 -name file5 \) -exec ls -l {} 2>/dev/null 
# Find IP in files
# https://www.shellhacks.com/regex-find-ip-addresses-file-grep/
find / -type f \( -name "8V2L" -o -name "bny0" -o -name "c4ZX" -o -name "D8B3" -o -name "FHl1" -o -name "oiM0" -o -name "PFbD" -o -name "rmfX" -o -name "SRSq" -o -name "uqyw" -o -name "v2Vb" -o -name "X1Uy" \) -exec sh -c 'ls -l "$1"; grep -qE "([0-9]{1,3}\.){3}[0-9]{1,3}" "$1" && echo "File contains an IP address: $1"' _ {} \; 2>/dev/null
find / -type f \( -name 8V2L -o -name bny0 -o -name c4ZX -o -name D8B3 -o -name FHl1 -o -name oiMO -o -name PFbD -o -name rmfX -o -name SRSq -o -name uqyw -o -name v2Vb -o -name X1Uy \) -exec egrep -o '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}' * {} \; 2>>/dev/null
# Look for marching SHA
find / -type f \( -name "8V2L" -o -name "bny0" -o -name "c4ZX" -o -name "D8B3" -o -name "FHl1" -o -name "oiMO" -o -name "PFbD" -o -name "rmfX" -o -name "SRSq" -o -name "uqyw" -o -name "v2Vb" -o -name "X1Uy" \) -exec sha1sum {} \; 2>/dev/null | grep "9d54da7584015647ba052173b84d45e8007eba94"
# Look for file with specific number of lines
find / -type f -name bny0 -exec wc -l {} \; 2>/dev/null
# Look for file id
-exec ls -ln {} | grep "502"



# Alternative
# https://sumanroy.gitbook.io/ctf-writeups/tryhackme-writeups/linux-ninja-skills-tryhackme
# https://infosecwriteups.com/tryhackme-ninja-skills-67726fa3956e