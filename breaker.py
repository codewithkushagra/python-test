data=b"xx\x11\x01\x03U\x08p\x930'\x826\x00!!\x00\x07\xc39\r\n"

l=[]


def divid(lo1,r):
     f=0
     for j in lo1:
          
         if f>1:
             r=r+j
         f+=1
     return r

def initial(data):
     o=0
     start=""
     packet_length=""
     protocol_number=""
     for i in data:

          if o<2:
               start=divid(hex(i),start)
          if o==2:
               packet_length=divid(hex(i),packet_length)
          if o==3:
               protocol_number=divid(hex(i),protocol_number)
               l.append(start)
               l.append(packet_length)
               l.append(protocol_number)
               if l[2]=='1':
                    login(data)
               elif l[2]=='22':
                    gps(data)
          o+=1


def gps(data):
     o=0
     date_time=""
     quantity=""
     latitude=""
     longitude=""
     speed=""
     course_status=""
     mcc=""
     mnc=""
     lac=""
     cell_id=""
     acc=""
     upload=""
     reupload=""
     sno=""
     error=""
     stop=""
     for i in data:
          k.append(hex(i))
          if o>3 and o<10:
               date_time=divid(hex(i),date_time)
          elif o==10:
               quantity=divid(hex(i),quantity)
          elif o>10 and o<15:
               latitude=divid(hex(i),latitude)
          elif o>14 and o<19:
               longitude=divid(hex(i),longitude)
          elif o==19:
               speed=divid(hex(i),speed)
          elif o>18 and o<21:
               course_status=divid(hex(i),course_status)
          elif o>20 and o<23:
               mcc=divid(hex(i),mcc)
          elif o==23:
               mnc=divid(hex(i),mnc)
          elif o>23 and o<26:
               lac=divid(hex(i),lac)
          elif o>25 and o<29:
               cell_id=divid(hex(i),cell_id)
          elif o==29:
               acc=divid(hex(i),acc)
          elif o==30:
               upload=divid(hex(i),upload)
          elif o==31:
               reupload=divid(hex(i),reupload)
          elif o>31 and o<34:
               sno=divid(hex(i),sno)
          elif o>33 and o<36:
               error=divid(hex(i),error)
          elif o>35:
               stop=divid(hex(i),stop)
          o+=1
     l.append(date_time)
     l.append(quantity)
     l.append(latitude)
     l.append(longitude)
     l.append(speed)
     l.append(course_status)
     l.append(mcc)
     l.append(mnc)
     l.append(lac)
     l.append(cell_id)
     l.append(acc)
     l.append(upload)
     l.append(reupload)
     l.append(sno)
     l.append(error)
     l.append(stop)
     
     return

def login(data):
     o=0
     imei=""
     codeid=""
     time_zone=""
     error=""
     sno=""
     stop=""
     for i in data:
          
          if o>3 and o<12:
               imei=divid(hex(i),imei)
          elif o>11 and o<14:
               codeid=divid(hex(i),codeid)
          elif o>13 and o<16:
               time_zone=divid(hex(i),time_zone)
          elif o>15 and o<18:
               sno=divid(hex(i),sno)
          elif o>17 and o<20:
               error=divid(hex(i),error)
          elif o>19:
               stop=divid(hex(i),stop)

          o+=1
     l.append(imei)
     l.append(codeid)
     l.append(time_zone)
     l.append(sno)
     l.append(error)
     l.append(stop)
initial(data)
print(l)

