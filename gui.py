import tkinter as tk
from member import *
from tkinter import *
from picture import *
import json


# function to add to JSON
def write_json(new_data, filename='data.json'):
    with open(filename,'r+') as file:
        # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data["members"].append(new_data)
        file_data["index"] += 1
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)

def run(p_id,p_name,p_lastname,p_categorie):
    global index
    p_id += 1
    picture(str(p_id), p_name, p_lastname, p_categorie)
    if(test(p_id,p_name,p_lastname,p_categorie)):
        mm = member(p_id, p_name, p_lastname, p_categorie)
        members.append(mm)
        index += 1

        varind = StringVar()
        varind.set(index+1)

        indlabel["text"] = varind.get()
        y =  {
            "Id": index,
            "Name": p_name,
            "LastName": p_lastname,
            "Categorie": p_categorie
        }
        write_json(y)

#lezen uit data.json voor gui runnen
members = []
# Opening JSON file
f = open('data.json', )

# returns JSON object as
# a dictionary
data = json.load(f)

# Iterating through the json
# list
index = data['index']
for i in data['members']:
    p_id = i['Id']
    p_name = i['Name']
    p_lastname = i['LastName']
    p_categorie = i['Categorie']
    mm = member(p_id, p_name, p_lastname, p_categorie)
    members.append(mm)

# Closing file
f.close()

#Gui
root = tk.Tk()
root.title("MFC")
root.iconbitmap("assets/logo.ico")
root.configure(bg='#434343')


tk.Label(root, text="Index",bg='#434343',fg='#ffffff',font='Helvetica 12').grid(row=0)
tk.Label(root,text="Naam",bg='#434343',fg='#ffffff',font='Helvetica 12').grid(row=1)
tk.Label(root, text="Achternaam",bg='#434343',fg='#ffffff',font='Helvetica 12').grid(row=2)
tk.Label(root, text="Categorie",bg='#434343',fg='#ffffff',font='Helvetica 12').grid(row=3)

OPTIONS = ["Volwassen","Jeugd","Vrouwen"]


var_name = StringVar(root)
var_last_name = StringVar(root)


e2 = tk.Entry(root,textvariable=var_name,bg='#ffffff',bd=0)
e3 = tk.Entry(root,textvariable=var_last_name,bg='#ffffff',bd=0)

var_categorie = StringVar(root)
var_categorie.set(OPTIONS[0])
o4 = OptionMenu(root,var_categorie,*OPTIONS)

#Functie run
buttonRun = Button(root,text="Run",width=20,command= lambda:run(index,var_name.get(),var_last_name.get(),var_categorie.get()))

buttonRun.grid(row=4,column=1,padx=10,pady=5)

indlabel = tk.Label(root, text=index+1,bg='#434343',fg='#ffffff',pady=5,font='Helvetica 14 bold')
indlabel.grid(row=0,column=1)
e2.grid(row=1, column=1,padx=10,pady=5)
e3.grid(row=2,column=1,padx=10,pady=5)
o4.grid(row=3,column=1,padx=10,pady=5)
o4["bd"] = 0
root.resizable(False,False)
root.mainloop()
