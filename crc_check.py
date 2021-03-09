hex_data='787811010355087093302782360021210007c3390d0a'
data=b"xx\x11\x01\x03U\x08p\x930'\x826\x00!!\x00\x07\xc39\r\n"
o=0
j=""
for i in hex_data:
     if o>3:
          j=j+i
     o+=1


print(j)


print(bytes.fromhex("11010355087093302782360021210007"))
