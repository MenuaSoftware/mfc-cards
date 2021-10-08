import tkinter as tk
from tkinter import filedialog

from PIL import ImageTk

from member import *
from tkinter import *
from picture import *
import json
from reportlab.lib.units import inch, cm


class gui:
    def __init__(self):
        self.file_name = ""
        self.members = []
        self.index = 0

    def guiStart(self):
        f = open('data.json', )
        data = json.load(f)

        self.index = data['index']
        for i in data['members']:
            p_id = i['Id']
            p_name = i['Name']
            p_lastname = i['LastName']
            p_categorie = i['Categorie']
            p_foto = i['Picture']
            mm = member(p_id, p_name, p_lastname, p_categorie,p_foto)
            self.members.append(mm)

        # Closing file
        f.close()

        # Gui
        self.root = tk.Tk()
        self.root.title("MFC")
        self.root.iconbitmap("assets/logo.ico")
        self.root.configure(bg='#434343')
        self.root.geometry("355x245")

        # Add image file
        bg = PhotoImage(file="assets/gui/main-bg.png")

        # Show image using label
        label1 = Label(self.root, image=bg,borderwidth=0, highlightthickness=0)
        label1.place(x=0, y=0)

        tk.Label(self.root, text="Naam", bg='#434343', fg='#ffffff', font='Helvetica 12').place(x=50,y=65)
        tk.Label(self.root, text="Achternaam", bg='#434343', fg='#ffffff', font='Helvetica 12').place(x=10,y=110)
        tk.Label(self.root, text="Categorie", bg='#434343', fg='#ffffff', font='Helvetica 12').place(x=25,y=155)

        browseimage = PhotoImage(file=r'assets/gui/browse-btn.png')
        browseimage = browseimage.subsample(20,20)

        self.msg_lbl = tk.Label(self.root, text="", bg='#434343', fg='#ffffff', font='Helvetica 8')
        # Create a File Explorer label
        self.label_file_explorer = Label(self.root, text="", bg='#434343', fg='#ffffff', font='Helvetica 6')
        button_explore = Button(self.root, text="Browse Files",bg="#2f2f2f", bd=0,image=browseimage ,command=self.browseFiles)
        self.label_file_explorer.place(x=5,y=215)
        button_explore.place(x=240,y=20)
        self.msg_lbl.place(x=280,y=215)

        searchimage = PhotoImage(file=r'assets/gui/search-btn.png')
        searchimage = searchimage.subsample(115,115)
        button_search = Button(self.root,text="Zoeken",bg="#2f2f2f", bd=0,image=searchimage,command=self.openNewWindow)
        button_search.place(x=320,y=20)

        OPTIONS = ["Volwassen", "Jeugd", "Vrouwen"]

        var_name = StringVar(self.root)
        var_last_name = StringVar(self.root)

        e2 = tk.Entry(self.root, textvariable=var_name, bg='#ffffff', bd=0)
        e3 = tk.Entry(self.root, textvariable=var_last_name, bg='#ffffff', bd=0)

        var_categorie = StringVar(self.root)
        var_categorie.set(OPTIONS[0])
        o4 = OptionMenu(self.root, var_categorie, *OPTIONS)

        # Functie run
        buttonRun = Button(self.root, text="Maken", bd=0, bg="#72b97e",fg="#ffffff",font='Helvetica 10 bold',command=lambda: self.run(self.index, var_name.get(), var_last_name.get(), var_categorie.get()))
        buttonRun.place(x=115,y=200,width=128)

        sortimage = PhotoImage(file=r'assets/gui/sort-btn.png')
        sortimage = sortimage.subsample(8,8)
        buttonImposition = Button(self.root, text="Imposition", bg="#2f2f2f", bd=0,image=sortimage,command=lambda: self.impos())
        buttonImposition.place(x=280,y=20)

        indrs = self.index +1
        self.indlabel = tk.Label(self.root, text="#"+str(indrs), bg='#2f2f2f', fg='#ffffff', pady=5, font='assets/TTOctosquaresEXP-BoldIt.ttf 16 bold')
        self.indlabel.place(x=15,y=12)

        e2.place(x=115,y=65,width=128,height=30)
        e3.place(x=115,y=110,width=128,height=30)
        o4.place(x=115,y=155,width=128,height=30)
        o4["bd"] = 0
        self.root.resizable(False, False)
        self.root.mainloop()

    def browseFiles(self):
        self.file_name = filedialog.askopenfilename(initialdir="/",title="Select a File",filetypes=(("PNG files","*.png*"),("all files","*.*")))
        base = os.path.basename(self.file_name)
        # Change label contents
        self.label_file_explorer.configure(text="File: " + base)


    def impos(self):
        lenFiles = len(os.listdir("results/kaarten"))
        if(lenFiles==0):
            self.msg_lbl["text"] = "no files found!"
            self.msg_lbl["fg"] = "#f55b5b"
        else:
            imposition()

    # on a button click
    def openNewWindow(self):

        self.newWindow = Toplevel(self.root)

        # sets the title of the
        # Toplevel widget
        self.newWindow.title("MFC")
        self.newWindow.iconbitmap("assets/logo.ico")
        self.newWindow.configure(bg='#434343')

        self.newWindow.resizable(False,False)
        # sets the geometry of toplevel

        var_txt = StringVar(self.newWindow)

        tk.Label(self.newWindow, text="Id:", bg='#434343', fg='#ffffff', font='Helvetica 12').grid(row=1)
        self.lbl_id = tk.Label(self.newWindow, text="", bg='#434343', fg='#ffffff', font='Helvetica 12 bold')
        self.lbl_id.grid(row=1,column=1)

        tk.Label(self.newWindow, text="Naam:", bg='#434343', fg='#ffffff', font='Helvetica 12').grid(row=2)
        self.lbl_name = tk.Label(self.newWindow, text="", bg='#434343', fg='#ffffff', font='Helvetica 12 bold')
        self.lbl_name.grid(row=2,column=1)

        tk.Label(self.newWindow, text="Achternaam:", bg='#434343', fg='#ffffff', font='Helvetica 12').grid(row=3)
        self.lbl_lastname = tk.Label(self.newWindow, text="", bg='#434343', fg='#ffffff', font='Helvetica 12 bold')
        self.lbl_lastname.grid(row=3, column=1)

        tk.Label(self.newWindow, text="Categorie:", bg='#434343', fg='#ffffff', font='Helvetica 12').grid(row=4)
        self.lbl_categorie = tk.Label(self.newWindow, text="", bg='#434343', fg='#ffffff', font='Helvetica 12 bold')
        self.lbl_categorie.grid(row=4, column=1)

        self.lbl_msg = tk.Label(self.newWindow,text="", fg='#ffffff', font='Helvetica 8')
        self.lbl_msg.grid(row=6)

        self.photo = PhotoImage()

        search_text = tk.Entry(self.newWindow, textvariable=var_txt, bg='#ffffff', bd=0)
        search_text.grid(row=0,padx=10, pady=5)

        btn_search = Button(self.newWindow,text="search",command=lambda :self.getInfo(var_txt.get()))
        btn_search.grid(row=0,column=1)

    def getInfo(self,p_id):
        p_id = p_id.capitalize()
        mmber = self.searchMember(p_id)
        if(mmber == False):
            self.lbl_msg["text"] = "Member not found!"
            self.lbl_msg["bg"] = "#f55b5b"
        else:
            self.lbl_msg["text"] = ""
            self.lbl_msg["bg"] = "#434343"
            self.lbl_id["text"] = mmber.id
            self.lbl_name["text"] = mmber.name
            self.lbl_lastname["text"] = mmber.lastname
            self.lbl_categorie["text"] = mmber.categorie
            if(mmber.foto != ""):
                img = Image.open(mmber.foto)
                img = img.resize((97, 124), Image.ANTIALIAS)
                img = ImageTk.PhotoImage(img)
                self.panel = Label(self.newWindow, image=img)
                self.panel.image = img
                self.panel.grid(row=5)
            else:
                self.panel.grid_forget()

    def run(self,p_id, p_name, p_lastname, p_categorie):
        if (checkFields(p_id, p_name, p_lastname, p_categorie)):
            p_id += 1
            self.index += 1
            varind = StringVar()
            varind.set(self.index + 1)
            im = None
            pic=""
            if(self.file_name != ""):
                passA4 = Image.open(self.file_name)
                width, height = passA4.size
                im = passA4.crop((0, 0, width - 2067, height - 2977))
                pic = 'results/passfotos/' + str(p_id) + "-" + p_name + '.png'
                im.save(pic)
                self.label_file_explorer["text"] = ""

            mm = member(p_id, p_name, p_lastname, p_categorie, pic)
            self.members.append(mm)

            self.indlabel["text"] = "#"+varind.get()
            y = {
                "Id": self.index,
                "Name": p_name,
                "LastName": p_lastname,
                "Categorie": p_categorie,
                "Picture": pic
            }
            write_json(y)
            self.msg_lbl["text"] = p_name + " toegevoegd!"
            self.msg_lbl["fg"] = "#76c96b"
            picture(str(p_id), p_name, p_lastname, p_categorie,im)
            self.file_name = ""
        else:
            self.msg_lbl["text"] = "Invalid fields!"
            self.msg_lbl["fg"] = "#f55b5b"


    def searchMember(self,p_id):
        for i in self.members:
            try:
                if(i.id == int(p_id)):
                    return i
            except:
                if(i.name == p_id):
                    return i
        return False


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

