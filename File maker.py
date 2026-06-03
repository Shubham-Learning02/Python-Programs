import itertools 
import os
print("Enter the name of the folder to create a folder or type end to exit.")
for i in itertools.repeat(None):
    a=input("Enter the name of the folder:")
    if(a.lower() != "end"):
        os.mkdir(f"{a}")
    else:
        print("Exiting")
    break


