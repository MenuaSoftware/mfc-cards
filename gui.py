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
        self.searchcount = 1
        self.searchlist = []

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
        self.root.title("Multi Fight Club")
        self.root.iconbitmap("assets/logo.ico")
        self.root.configure(bg='#434343')
        self.root.geometry("1200x676+0+0")

        # Add image file
        bg = PhotoImage(file="assets/gui/theme.png")

        # Show image using label
        label1 = Label(self.root, image=bg,borderwidth=0, highlightthickness=0)
        label1.place(x=0, y=0)

        dashboardimage = PhotoImage(file="assets/gui/Dashboard-select.png")
        self.dashselect = Button(self.root,image=dashboardimage,borderwidth=0,highlightthickness=0,command = self.navDashboard)
        self.dashselect.place(x=0,y=72)

        membersiamge = PhotoImage(file="assets/gui/Members-unselect.png")
        self.membersselect = Button(self.root,image=membersiamge,borderwidth=0,highlightthickness=0,command=self.navMembers)
        self.membersselect.place(x=0,y=124)

        #createimage wd show
        crwd = PhotoImage(file="assets/gui/createmember-wd.png")
        self.labelcreate = Label(self.root,image=crwd,borderwidth=0,highlightthickness=0)
        self.labelcreate.place(x=204,y=72)

        #searchmember wd
        srchmb = PhotoImage(file="assets/gui/searchmember-wd.png")
        self.labelsearch = Label(self.root,image=srchmb,borderwidth=0,highlightthickness=0)

        var_txt = StringVar(self.root)
        self.search_text = tk.Entry(self.root, textvariable=var_txt, bg='#ffffff', bd=0,width=18)

        searchimage = PhotoImage(file=r'assets/gui/search-btn.png')
        searchimage = searchimage.subsample(1, 1)
        self.btn_search = Button(self.root, text="Zoek", bg="#ffffff", bd=0, image=searchimage, command=lambda :self.getInfo(var_txt.get()))
        self.btn_search.image = searchimage

        self.lbl_id = tk.Label(self.root, text="", bg='#ffffff', fg='#1f1f1f', font='Helvetica 16 bold')
        self.lbl_name = tk.Label(self.root, text="", bg='#ffffff', fg='#1f1f1f', font='Helvetica 14 bold')
        self.lbl_lastname = tk.Label(self.root, text="", bg='#ffffff', fg='#1f1f1f', font='Helvetica 14 bold')
        self.lbl_categorie = tk.Label(self.root, text="", bg='#ffffff', fg='#1f1f1f', font='Helvetica 14 bold')

        addimage = PhotoImage(file=r'assets/gui/browse-btn.png')
        addimage = addimage.subsample(2,2)
        self.btn_addimage = Button(self.root, bg="#ffffff", bd=0, image=addimage, command=lambda :self.changeImage(self.currid))
        self.btn_addimage.image = addimage

        addcardimage = PhotoImage(file=r'assets/gui/addcard-btn.png')
        addcardimage = addcardimage.subsample(1,1)
        self.btn_addcardimage = Button(self.root, bg="#ffffff", bd=0, image=addcardimage, command=lambda :self.addcardimage(self.currid))
        self.btn_addcardimage.image = addcardimage

        editimage = PhotoImage(file=r'assets/gui/edit-btn.png')
        editimage = editimage.subsample(1,1)
        self.btn_editimage = Button(self.root, bg="#ffffff", bd=0, image=editimage, command=lambda :self.changeUser(self.currid))
        self.btn_editimage.image = editimage

        self.btn_saveimage = Button()
        self.name_text = tk.Entry()
        self.lastname_text = tk.Entry()
        self.categorie_option = Button()

        leftimage = PhotoImage(file=r'assets/gui/left-btn.png')
        leftimage = leftimage.subsample(2,2)
        self.btn_left = Button(self.root, bg="#ffffff", bd=0, image=leftimage,command= lambda: self.left(self.searchlist, self.searchcount))
        self.btn_left.image = leftimage

        rightimage = PhotoImage(file=r'assets/gui/right-btn.png')
        rightimage = rightimage.subsample(2, 2)
        self.btn_right = Button(self.root, bg="#ffffff", bd=0, image=rightimage,command= lambda: self.next(self.searchlist, self.searchcount))
        self.btn_right.image = rightimage

        self.lbl_count = Label(self.root, text="", bg='#ffffff', fg='#1f1f1f', font='Helvetica 13 bold')
        self.lbl_count["text"] = ""
        self.lbl_count.place(x=555, y=458)

        self.lbl_msg = tk.Label(self.root, text="", bg="#ffffff", font='Helvetica 8')

        browseimage = PhotoImage(file=r'assets/gui/browse-btn.png')
        browseimage = browseimage.subsample(1,1)

        excelimage = PhotoImage(file=r'assets/gui/excel-btn.png')
        excelimage = excelimage.subsample(1,1)

        imagewd = PhotoImage(file="assets/gui/image-wd.png")
        self.imagewd = Label(self.root,image=imagewd,borderwidth=0,highlightthickness=0)

        self.msg_lbl = tk.Label(self.root, text="", bg='#ffffff', fg='#1f1f1f', font='Helvetica 8')
        # Create a File Explorer label
        self.label_file_explorer = Label(self.root, text="", bg='#ffffff', fg='#1f1f1f', font='Helvetica 6')
        self.button_explore = Button(self.root, text="Browse Files",bg="#ffffff", bd=0,image=browseimage ,command=self.browseFiles)
        self.label_file_explorer.place(x=430,y=230)
        self.button_explore.place(x=430,y=190)
        self.msg_lbl.place(x=270,y=530)

        self.btn_excel = Button(self.root, text="browse excel",bg="#ffffff", bd=0,image=excelimage ,command=self.readExcel)
        self.btn_excel.place(x=396,y=555)

        self.OPTIONS = ["Volwassen", "Jeugd", "Vrouwen"]

        var_name = StringVar(self.root)
        var_last_name = StringVar(self.root)

        self.e2 = tk.Entry(self.root, textvariable=var_name, bg='#ffffff', highlightthickness=2,bd=0)
        self.e2.config(highlightbackground="#1f1f1f", highlightcolor="#1f1f1f")
        self.e3 = tk.Entry(self.root, textvariable=var_last_name, bg='#ffffff', highlightthickness=2 ,bd=0)
        self.e3.config(highlightbackground="#1f1f1f", highlightcolor="#1f1f1f")

        var_categorie = StringVar(self.root)
        var_categorie.set(self.OPTIONS[0])
        self.o4 = OptionMenu(self.root, var_categorie, *self.OPTIONS)

        # Functie run
        self.buttonRun = Button(self.root, text="Create", bd=0, bg="#72b97e",fg="#ffffff",font='Helvetica 10 bold',command=lambda: self.run(self.index, var_name.get(), var_last_name.get(), var_categorie.get()))

        self.buttonRun.place(x=270,y=555,width=105,height=38)

        sortimage = PhotoImage(file=r'assets/gui/sort-btn.png')
        sortimage = sortimage.subsample(1,1)
        self.buttonImposition = Button(self.root, text="Imposition", bg="#ffffff", bd=0,image=sortimage,command=lambda: self.impos())
        self.buttonImposition.place(x=445,y=555)

        indrs = self.index +1
        self.indlabel = tk.Label(self.root, text="#"+str(indrs), bg='#ffffff', fg='#1f1f1f', pady=5, font='assets/SourceSansPro-Bold.ttf')
        self.indlabel.place(x=270,y=190)

        self.e2.place(x=270,y=276,width=210,height=38)
        self.e3.place(x=270,y=381,width=210,height=38)
        self.o4.place(x=270,y=486,width=210,height=38)
        self.o4["highlightthickness"] = 2
        self.o4.config(highlightbackground="#1f1f1f", highlightcolor="#1f1f1f")
        self.o4["bd"] = 0

        self.panel = Label()

        self.root.resizable(False, False)
        self.root.mainloop()

    def navMembers(self):
        #navbar dashboard
        self.dashselect.place_forget()
        dashimage = PhotoImage(file="assets/gui/Dashboard-unselect.png")
        self.dashselect.image = dashimage
        self.dashselect["image"]=dashimage
        self.dashselect.place(x=0,y=72)

        #navbar members
        self.membersselect.place_forget()
        membimage = PhotoImage(file="assets/gui/Members-select.png")
        self.membersselect.image = membimage
        self.membersselect["image"] = membimage
        self.membersselect.place(x=0,y=124)

        #hiding main dash
        self.labelcreate.place_forget()
        self.e3.place_forget()
        self.e2.place_forget()
        self.o4.place_forget()
        self.msg_lbl.place_forget()
        self.label_file_explorer.place_forget()
        self.indlabel.place_forget()
        self.buttonRun.place_forget()
        self.buttonImposition.place_forget()
        self.button_explore.place_forget()
        self.btn_excel.place_forget()
        self.imagewd.place_forget()
        self.panel.place_forget()

        #showing member dash
        self.labelsearch.place(x=204, y=72)
        self.search_text.place(x=460,y=110,width=200)
        self.btn_search.place(x=688,y=100)

        self.lbl_id.place(x=522,y=190)
        self.lbl_name.place(x=520,y=255)
        self.lbl_lastname.place(x=520,y=335)
        self.lbl_categorie.place(x=520,y=415)
        self.lbl_msg.place(x=520,y=460)

        self.btn_addimage.place(x=248,y=108)
        self.btn_addcardimage.place(x=313,y=100)
        self.btn_editimage.place(x=385,y=100)

        self.lbl_count["text"] = ""
        self.lbl_count.place(x=555, y=458)

    def navDashboard(self):
        #navbar members
        self.membersselect.place_forget()
        membimage = PhotoImage(file="assets/gui/Members-unselect.png")
        self.membersselect.image = membimage
        self.membersselect["image"] = membimage
        self.membersselect.place(x=0,y=124)

        #navbar dashboard
        self.dashselect.place_forget()
        dashimage = PhotoImage(file="assets/gui/Dashboard-select.png")
        self.dashselect.image = dashimage
        self.dashselect["image"]=dashimage
        self.dashselect.place(x=0,y=72)

        #hiding members dash
        self.labelsearch.place_forget()
        self.search_text.place_forget()
        self.btn_search.place_forget()

        self.currid = 0
        self.lbl_id["text"] = ""
        self.lbl_name["text"] = ""
        self.lbl_lastname["text"] = ""
        self.lbl_categorie["text"] = ""
        self.lbl_msg.place_forget()

        self.btn_addimage.place_forget()
        self.btn_addcardimage.place_forget()
        self.btn_editimage.place_forget()

        self.btn_saveimage.place_forget()
        self.name_text.place_forget()
        self.panel.place_forget()
        self.lastname_text.place_forget()
        self.categorie_option.place_forget()

        self.btn_left.place_forget()
        self.btn_right.place_forget()
        self.lbl_count.place_forget()

        #main wd
        self.labelcreate.place(x=204,y=72)
        self.e3.place(x=270,y=381,width=210,height=38)
        self.e2.place(x=270,y=276,width=210,height=38)
        self.o4.place(x=270,y=486,width=210,height=38)
        self.msg_lbl.place(x=270,y=530)
        self.label_file_explorer.place(x=430,y=230)
        self.indlabel.place(x=270,y=190)
        self.buttonRun.place(x=270,y=555,width=105,height=38)
        self.buttonImposition.place(x=445,y=555)
        self.button_explore.place(x=430,y=190)
        self.btn_excel.place(x=396,y=555)

    def browseFiles(self):
        self.file_name = filedialog.askopenfilename(initialdir="/",title="Select a File",filetypes=(("PNG files","*.png*"),("all files","*.*")))
        base = os.path.basename(self.file_name)
        # Change label contents
        self.label_file_explorer.configure(text="File: " + base)

        self.imagewd.place(x=550,y=75)
        passA4 = Image.open(self.file_name)
        width, height = passA4.size
        im = passA4.crop((0, 0, width - 2067, height - 2977))
        im = im.resize((194, 248), Image.ANTIALIAS)
        im = ImageTk.PhotoImage(im)

        self.panel = Label(self.root, borderwidth=0, highlightthickness=0)
        self.panel["image"] = im
        self.panel.image = im
        self.panel.place(x=605, y=130)
        #foto opladen

    def impos(self):
        lenFiles = len(os.listdir("results/kaarten"))
        if(lenFiles==0):
            self.msg_lbl["text"] = "no files found!"
            self.msg_lbl["fg"] = "#f55b5b"
        else:
            self.msg_lbl["text"] = "Sorting done!"
            self.msg_lbl["fg"] = "#76c96b"
            imposition()

    def saveEdit(self,p_id,p_name,p_lastname,p_categorie):
        self.btn_left.place_forget()
        self.btn_right.place_forget()
        self.lbl_count["text"] = ""
        #hide everything -> all textboxes and unhide lbls
        self.btn_saveimage.place_forget()
        self.btn_editimage.place(x=385, y=100)
        self.name_text.place_forget()
        self.lastname_text.place_forget()
        self.categorie_option.place_forget()

        self.lbl_name["text"] = p_name
        self.lbl_name.place(x=520,y=255)
        
        self.lbl_lastname["text"] = p_lastname
        self.lbl_lastname.place(x=520,y=335)

        self.lbl_categorie["text"] = p_categorie
        self.lbl_categorie.place(x=520,y=415)
        mber = self.searchMember(p_id)
        #change json
        with open('data.json') as file:
            data = json.load(file)
        for i in data['members']:
            if mber.id == i['Id']:
                i['Name'] = p_name
                i['LastName'] = p_lastname
                i['Categorie'] = p_categorie
        with open('data.json', 'w') as file:
            json.dump(data, file, indent=2)

        #change member
        mber.name = p_name
        mber.lastname = p_lastname
        mber.categorie = p_categorie

        mmber = self.searchlist

        self.lbl_msg["text"] = ""
        self.lbl_id["text"] = "#" + str(mmber[self.searchcount-1].id)
        self.lbl_name["text"] = mmber[self.searchcount-1].name
        self.lbl_lastname["text"] = mmber[self.searchcount-1].lastname
        self.lbl_categorie["text"] = mmber[self.searchcount-1].categorie
        if (mmber[self.searchcount-1].foto != ""):
            img = Image.open(mmber[self.searchcount-1].foto)
            img = img.resize((235, 303), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(img)
            self.panel = Label(self.root, borderwidth=0, highlightthickness=0)
            self.panel["image"] = img
            self.panel.image = img
            self.panel.place(x=257, y=189)

        self.btn_left.place(x=530, y=460)
        self.lbl_count["text"] = str(self.searchcount) + "/" + str(len(self.searchlist))
        self.btn_right.place(x=590, y=460)

    def changeUser(self,p_id):
        self.btn_left.place_forget()
        self.btn_right.place_forget()
        self.lbl_count["text"] = ""
        mber = self.searchMember(p_id)
        #hide all
        self.btn_editimage.place_forget()
        self.lbl_name.place_forget()
        self.lbl_lastname.place_forget()
        self.lbl_categorie.place_forget()

        #make entry's
        name_var = StringVar(self.root)
        self.name_text = tk.Entry(self.root, textvariable=name_var, bg='#ffffff', bd=0,highlightthickness=2 ,width=18)
        self.name_text.config(highlightbackground="#1f1f1f", highlightcolor="#1f1f1f")
        self.name_text.insert(END, mber.name)
        self.name_text.place(x=520,y=255,width=200,height=40)

        lastname_var = StringVar(self.root)
        self.lastname_text = tk.Entry(self.root, textvariable=lastname_var, bg='#ffffff', highlightthickness=2, bd=0, width=18)
        self.lastname_text.config(highlightbackground="#1f1f1f", highlightcolor="#1f1f1f")
        self.lastname_text.insert(END, mber.lastname)
        self.lastname_text.place(x=520,y=335,width=200,height=40)

        categorie_var = StringVar(self.root)
        for k in range(len(self.OPTIONS)):
            if mber.categorie == self.OPTIONS[k]:
                categorie_var.set(self.OPTIONS[k])

        self.categorie_option = OptionMenu(self.root, categorie_var, *self.OPTIONS)
        self.categorie_option["bd"] = 0
        self.categorie_option.place(x=520,y=415)

        saveimage = PhotoImage(file=r'assets/gui/save-btn.png')
        saveimage = saveimage.subsample(1,1)
        self.btn_saveimage = Button(self.root, bg="#ffffff", bd=0, image=saveimage, command=lambda: self.saveEdit(p_id, name_var.get(), lastname_var.get(), categorie_var.get()))
        self.btn_saveimage.image = saveimage
        self.btn_saveimage.place(x=385,y=100)

    def addcardimage(self,p_id):
        mber = self.searchMember(p_id)
        if mber.foto == "":
            picture(str(mber.id), mber.name, mber.lastname, mber.categorie)
        else:
            picture(str(mber.id), mber.name, mber.lastname, mber.categorie, mber.foto)
        self.lbl_msg['text'] = "Succesvol aangemaakt!"
        self.lbl_msg['fg'] = "#76c96b"

    def changeImage(self,p_member):
        mmber = self.searchMember(p_member)
        if(mmber):
            file_name = filedialog.askopenfilename(initialdir="/",title="Select a File",filetypes=(("PNG files","*.png*"),("all files","*.*")))
            passA4 = Image.open(file_name)
            width, height = passA4.size
            im = passA4.crop((0, 0, width - 2067, height - 2977))
            pic = 'results/passfotos/' + str(mmber.id) + "-" + mmber.name + '.png'
            im.save(pic)
            #toevoegen json
            self.replaceFoto(mmber.id,pic)
            #toevoegen member
            mmber.foto = pic
            im = im.resize((235, 303), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(im)
            self.panel["image"] = img
            self.panel.image = img
            self.lbl_msg['text'] = "foto succesvol veranderd!"
            self.lbl_msg['fg'] = "#76c96b"

    def replaceFoto(self,p_id,p_picture):
        with open('data.json') as file:
            data = json.load(file)

        for i in data['members']:
            if p_id == i['Id']:
                i['Picture'] = p_picture

        with open('data.json', 'w') as file:
            json.dump(data, file, indent=2)

    def getInfo(self,p_id):
        self.panel.place_forget()
        self.lbl_id["text"] = ""
        self.lbl_name["text"] = ""
        self.lbl_lastname["text"] = ""
        self.lbl_categorie["text"] = ""
        self.lbl_count["text"] = ""
        self.btn_left.place_forget()
        self.btn_right.place_forget()

        self.searchcount = 1
        self.searchlist = []

        p_id = p_id.capitalize()
        mmber = self.searchmoremembers(p_id)

        if(mmber == False):
            self.lbl_msg["text"] = "Member not found!"
            self.lbl_msg["fg"] = "#f55b5b"
        elif(isinstance(mmber,list)):
            #show arrows to go left right etc:
            self.currid = mmber[0].id
            self.lbl_msg["text"] = ""
            self.lbl_id["text"] = "#" + str(mmber[0].id)
            self.lbl_name["text"] = mmber[0].name
            self.lbl_lastname["text"] = mmber[0].lastname
            self.lbl_categorie["text"] = mmber[0].categorie
            if (mmber[0].foto != ""):
                img = Image.open(mmber[0].foto)
                img = img.resize((235, 303), Image.ANTIALIAS)
                img = ImageTk.PhotoImage(img)
                self.panel = Label(self.root, borderwidth=0, highlightthickness=0)
                self.panel["image"] = img
                self.panel.image = img
                self.panel.place(x=257, y=189)


            self.btn_left.place(x=530,y=460)
            self.searchlist = mmber
            self.lbl_count["text"] = str(self.searchcount) + "/" + str(len(self.searchlist))
            self.searchcount = 1
            self.btn_right.place(x=590,y=460)
        else:
            self.btn_left.place_forget()
            self.btn_right.place_forget()
            self.lbl_count["text"] = ""
            self.lbl_msg["text"] = ""
            self.lbl_id["text"] = "#" + str(mmber.id)
            self.lbl_name["text"] = mmber.name
            self.lbl_lastname["text"] = mmber.lastname
            self.lbl_categorie["text"] = mmber.categorie
            self.currid = mmber.id
            if(mmber.foto != ""):
                img = Image.open(mmber.foto)
                img = img.resize((235, 303), Image.ANTIALIAS)
                img = ImageTk.PhotoImage(img)
                self.panel = Label(self.root, borderwidth=0, highlightthickness=0)
                self.panel["image"] = img
                self.panel.image = img
                self.panel.place(x=257,y=189)
            else:
                self.panel.place_forget()

    def next(self,list,curr):
        lengte = len(list)
        if(curr< (lengte)):#index begint met 1 bij curr
            self.searchcount +=1
            self.lbl_count["text"] = str(self.searchcount) + "/" + str(len(self.searchlist))
            mmber = list[curr]
            self.currid = mmber.id
            self.lbl_msg["text"] = ""
            self.lbl_id["text"] = "#" + str(mmber.id)
            self.lbl_name["text"] = mmber.name
            self.lbl_lastname["text"] = mmber.lastname
            self.lbl_categorie["text"] = mmber.categorie
            self.currid = mmber.id
            if(mmber.foto != ""):
                img = Image.open(mmber.foto)
                img = img.resize((235, 303), Image.ANTIALIAS)
                img = ImageTk.PhotoImage(img)
                self.panel = Label(self.root, borderwidth=0, highlightthickness=0)
                self.panel["image"] = img
                self.panel.image = img
                self.panel.place(x=257,y=189)
            else:
                self.panel.place_forget()


    def left(self,list,curr):
        if(curr > 1):#index begint met 1 bij curr
            self.searchcount -= 1
            self.lbl_count["text"] = str(self.searchcount) + "/" + str(len(self.searchlist))
            mmber = list[curr-2]
            self.currid = mmber.id
            self.lbl_msg["text"] = ""
            self.lbl_id["text"] = "#" + str(mmber.id)
            self.lbl_name["text"] = mmber.name
            self.lbl_lastname["text"] = mmber.lastname
            self.lbl_categorie["text"] = mmber.categorie
            self.currid = mmber.id
            if(mmber.foto != ""):
                img = Image.open(mmber.foto)
                img = img.resize((235, 303), Image.ANTIALIAS)
                img = ImageTk.PhotoImage(img)
                self.panel = Label(self.root, borderwidth=0, highlightthickness=0)
                self.panel["image"] = img
                self.panel.image = img
                self.panel.place(x=257,y=189)
            else:
                self.panel.place_forget()

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

            p_name = p_name.capitalize()
            p_lastname = p_lastname.capitalize()

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

    def searchmoremembers(self,p_id):
        list = []
        for i in self.members:
            try:
                if(i.id == int(p_id)):
                    return i
            except:
                if(i.name == p_id):
                    list.append(i)
        if(len(list)>0):
            if(len(list) == 1):
                return list[0]
            else:
                return list
        else:
            return False

    def searchMember(self,p_id):
        for i in self.members:
            try:
                if(i.id == int(p_id)):
                    return i
            except:
                if(i.name == p_id):
                    return i
        return False

    def readExcel(self):
        file = filedialog.askopenfilename(initialdir="/",title="Select a File",filetypes=(("EXCEL files","*.xlsx*"),("all files","*.*")))
        df = pd.read_excel(file)
        lenUs = len(df['Naam'])
        for i in range(lenUs):
            self.index += 1
            p_id = self.index
            p_name = df['Naam'][i]
            p_lastname = df['Achternaam'][i]
            p_categorie = df['Categorie'][i]

            p_name = p_name.capitalize()
            p_lastname = p_lastname.capitalize()
            p_categorie = p_categorie.capitalize()

            im = None
            pic=""

            mm = member(p_id, p_name, p_lastname, p_categorie, pic)
            self.members.append(mm)

            y = {
                "Id": self.index,
                "Name": p_name,
                "LastName": p_lastname,
                "Categorie": p_categorie,
                "Picture": pic
            }
            write_json(y)
            picture(str(p_id), p_name, p_lastname, p_categorie,im)
        varind = StringVar()
        varind.set(self.index+1)

        self.indlabel['text'] = "#" + varind.get()
        self.msg_lbl["fg"] = "#76c96b"
        self.msg_lbl['text'] = "Succesvol allemaal toegevoegd"

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



