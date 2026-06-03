ww=input("Enter a word:")
f=input("Choose to encode or decode:")
def co(w):
    w=w.lower()
    fin=""
    l=len(w)
    if(l<3):
        for i in reversed(w):
            fin=fin+i
    else:
        for i in range(1,l):
            fin+=w[i]
        fin+=w[0]
        print(fin)
        fin="ajf"+fin+"sjd"
    return fin
def deco(a):
    fin=""
    l=len(a)
    if(l<3):
        for i in reversed(a):
            fin=fin+i
    else:        
        fin=a[3:l-3]
        ll=len(fin)
        fin=fin[ll-1]+fin[0:ll-1]
    return fin
if(f.lower()=="encode"):
    s=co(ww)
    print(s)
elif(f.lower()=="decode"):
    s=deco(ww)
    print(s)
else:
    print("Error Input")