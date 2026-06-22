#imports:
import tkinter as tk
import subprocess,sys


#checking if the package "tabulate" is already downloaded or not and downloads if it is not already installed:
try: 
    from tabulate import tabulate
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "tabulate"])
import json


#initialising files for json:
global r,n,cla,p,c,m
try:
    with open("students.json", "r") as f:
        data = json.load(f)

    r = data["r"]
    n = data["n"]
    cla = data["cla"]
    p = data["p"]
    c = data["c"]
    m = data["m"]
except FileNotFoundError:
    r = []
    n = []
    cla = []
    p = []
    c = []
    m = []


#function to save data in storage using json:
def save_data():
    data = {"r": r,"n": n,"cla": cla,"p": p,"c": c,"m": m}

    with open("students.json", "w") as f:
        json.dump(data, f, indent=4)


#global files:
global roll,name,classs,phy,chem,math,form,view
global ro,up,d


#Base window:
root = tk.Tk()

root.title("Student Manager")
root.geometry("1500x1000")

label=tk.Label(root,text="Select an option to perform",fg="yellow",bg="red",font=("Arial",24,"bold italic"))
label.pack()


#Add A Student:
def AS():
    global roll,name,classs,phy,chem,math,form

    form=tk.Tk()
    form.title("Add Student")
    form.geometry("1500x1000")


    label=tk.Label(form,text="Enter the Roll Number of the Student:",font=("Arial",18))
    label.pack()
    roll=tk.Entry(form)
    roll.pack()
    
    label=tk.Label(form,text="Enter the Name of the Student: ",font=("Arial",18))
    label.pack()
    name=tk.Entry(form)
    name.pack() 

    label=tk.Label(form,text="Enter the Class of the Student: ",font=("Arial",18))
    label.pack()
    classs=tk.Entry(form)
    classs.pack()

    label=tk.Label(form,text="Marks in Physics ",font=("Arial",18))
    label.pack()
    phy=tk.Entry(form)
    phy.pack()

    label=tk.Label(form,text="Marks in Chemistry",font=("Arial",18))
    label.pack()
    chem=tk.Entry(form)
    chem.pack()

    label=tk.Label(form,text="Marks in Mathematics: ",font=("Arial",18))
    label.pack()
    math=tk.Entry(form)
    math.pack()

    save=tk.Button(form,text="Save",command=saeve)
    save.pack()
       

#Saves the student data entered in Add Student
def saeve():
    global roll,name,classs,phy,chem,math,form
    
    if roll.get() in r:
        label=tk.Label(form,text="Student already present. Switch to Update Student Detail to update or change details",font=("Arial",18))
        label.pack()
        return
    else:
        r.append(roll.get())
        n.append(name.get())
        cla.append(classs.get())
        p.append(phy.get())
        c.append(chem.get())
        m.append(math.get())
        label=tk.Label(form,text="Student added sucessfully")
        label.pack()
        save_data()


#View All Student:
def VS():
    dis=tk.Tk()
    dis.title("Total Record")
    dis.geometry("1500x1000")

    headers=["Roll Number","Name","Class","Physics","Chemistry","Maths"]
    table = tabulate(zip(r,n,cla,p,c,m),headers=headers, tablefmt="grid")
    label=tk.Label(dis,text=table,font=("Courier New",10)).pack()



#View A Student:
def VAS():
    global view,ro
    view=tk.Tk()
    view.title("Student Record")
    view.geometry("1500x1000")

    label=tk.Label(view,text="Enter the Roll Number of the Student:",font=("Arial",18))
    label.pack()
    ro=tk.Entry(view)
    ro.pack()

    save=tk.Button(view,text="Save",command=vie)
    save.pack()


#Views the data of A particular student entered in VAS()
def vie():
    global view,ro
    if ro.get() in r:   
        headers=["Roll Number","Name","Class","Physics","Chemistry","Maths"]
        rol=r.index(ro.get())
        table = tabulate([[r[rol],n[rol],cla[rol],p[rol],c[rol],m[rol]]],headers=headers, tablefmt="grid")
        label=tk.Label(view,text=table,font=("Courier New",10)).pack()
    else:
        label=tk.Label(view,text="Student Not Present",font=("Arial",18))
        label.pack()


#Update Student Record:
def US():
    global up,ro
    up=tk.Tk()
    up.title("Update Student Record")
    up.geometry("1500x1000")

    label=tk.Label(up,text="Enter the Roll Number of the Student:",font=("Arial",18))
    label.pack()
    ro=tk.Entry(up)
    ro.pack()

    save=tk.Button(up,text="Confirm",command=upd)
    save.pack()


#Saves the updated student data in the storage:
def sve():
    global ro,up
    global roll,name,classs,phy,chem,math
    global r,n,cla,p,c,m
    cg=r.index(ro.get().strip())
    r[cg]=ro.get()
    n[cg]=name.get()
    cla[cg]=classs.get()
    p[cg]=phy.get()
    c[cg]=chem.get()
    m[cg]=math.get()
    label=tk.Label(up,text="Student Updated sucessfully")
    label.pack()
    save_data()
    

#Takes the new data for the student to update and sends to sve():
def upd():
    global roll,name,classs,phy,chem,math,up,ro
    
    if ro.get() in r:
        label=tk.Label(up,text="Enter the Name of the Student: ",font=("Arial",18))
        label.pack()
        name=tk.Entry(up)
        name.pack() 

        label=tk.Label(up,text="Enter the Class of the Student: ",font=("Arial",18))
        label.pack()
        classs=tk.Entry(up)
        classs.pack()

        label=tk.Label(up,text="Marks in Physics ",font=("Arial",18))
        label.pack()
        phy=tk.Entry(up)
        phy.pack()

        label=tk.Label(up,text="Marks in Chemistry",font=("Arial",18))
        label.pack()
        chem=tk.Entry(up)
        chem.pack()

        label=tk.Label(up,text="Marks in Mathematics: ",font=("Arial",18))
        label.pack()
        math=tk.Entry(up)
        math.pack()

        save=tk.Button(up,text="Save",command=sve)
        save.pack()
    else:
        label=tk.Label(up,text="Student Not Present In Databaase",font=("Arial",18))
        label.pack()
        return
    save_data()


#Deletes the data of a student:
def DS():
    global d,ro
    global r,n,cla,p,c,m
    d=tk.Tk()
    d.title("Delete Student Record")
    d.geometry("1500x1000")

    label=tk.Label(d,text="Enter the Roll Number of the Student:",font=("Arial",18))
    label.pack()
    ro=tk.Entry(d)
    ro.pack()

    save=tk.Button(d,text="Save",command=dela)
    save.pack()


#Makes changes in the storage:
def dela():
        global r,n,cla,p,c,m,ro
        if ro.get() in r:
            indx=r.index(ro.get().strip())
            r.pop(indx)
            cla.pop(indx)
            n.pop(indx)
            p.pop(indx)
            c.pop(indx)
            m.pop(indx)
            label=tk.Label(d,text="Student deleted sucessfully")
            label.pack()
        else:
            label=tk.Label(d,text="Roll Number not found")
            label.pack()
            return
        save_data()
        

#Base window buttons:
button=tk.Button(root,text="Add Student",command=AS)
button.pack()

button=tk.Button(root,text="View All Students",command=VS)
button.pack()

button=tk.Button(root,text="View A Student",command=VAS)
button.pack()

button=tk.Button(root,text="Update Student Record",command=US)
button.pack()

button=tk.Button(root,text="Delete A Student",command=DS)
button.pack()
root.mainloop() 