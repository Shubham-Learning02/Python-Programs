import time
hrs=time.strftime('%H')
tim=time.strftime('%H:%M')
hr=(int)(hrs)   
if(hr>=0):
    if(hr<12):
        sr="Good Morning"
elif(hr>=12):
    if(hr<5):
        sr="Good Afternoon"
else:
    sr="Good Evening"
print(tim)
print(sr)
if(sr=="Good Morning"):
    ga=tim+" A.M."
elif(sr=="Good Afternoon"):
    g=(int)(tim)-12
    ga=(str)(g)+" P.M."
else:
    g=(int)(tim)-12
    ga=(str)(g)+" P.M."
print(ga)
