hex_data='787811010355087093302782360021210007c3390d0a'
k=[]

def login(hex_data):
     g=""
     o=0
     for i in hex_data:
          if o>7 and o<24:
               g=g+i
               
          if o==24:
               k.append(g)
               g=""
          if o>23 and o<28:
               g=g+i
          if o==28:
               k.append(g)
               g=""
          if o>27 and o<32:
               g=g+i
          if o==32:
               k.append(g)
               g=""
          if o>31 and o<36:
               g=g+i
          if o==36:
               k.append(g)
               g=""
          if o>35 and o<40:
               g=g+i
          if o==40:
               k.append(g)
               g=""
          if o>39 and o<44:
               g=g+i
          if o==43:
               k.append(g)
               g=""
          o+=1
     return


def initial(hex_data):
     o=0
     g=""
     for i in hex_data:
          if o<4:
               g=g+i
          if o==4:
               k.append(g)
               g=""
          if o>3 and o<6:
               g=g+i
          if o==6:
               k.append(g)
               g=""
          if o>5 and o<8:
               g=g+i
          if o==8:
               k.append(g)
               g=""
          o+=1
     if k[2]=='01':
          login(hex_data)
     elif k[2]=='22':
          gps(hex_data)
     return k

print(initial(hex_data))
print(k[len(k)-3])
