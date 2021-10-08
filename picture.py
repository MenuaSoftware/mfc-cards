from PIL import Image, ImageFont, ImageDraw
import os, os.path
import math
import json
from pathlib import Path
import shutil

class picture:
    def __init__(self,p_id,p_naam,p_achternaam,p_categorie,p_im = None):
        self.drawPic(p_id,p_naam,p_achternaam,p_categorie,p_im)

    def drawPic(self,id, naam,achternaam,categorie,p_im = None):
        if(id != "" and naam != "" and achternaam != "" and categorie != ""):
            lstname = 55
            mnt = 60
            color = (0,0,0)
            color2 = (43,43,43)
            id_font = ImageFont.truetype('assets/TTOctosquaresEXP-BoldIt.ttf', 60) #font
            font = ImageFont.truetype('assets/TTOctosquaresEXP-BoldIt.ttf', 60) #font

            # Categorie:
            categorie = categorie.lower()
            if(categorie == "volwassen"):
                categorie_text = "Volwassen"
                my_image = Image.open("assets/template_blue.png")
            elif(categorie == "jeugd"):
                categorie_text = "Jeugd"
                my_image = Image.open("assets/template_green.png")
            elif(categorie == "vrouwen"):
                categorie_text = "Vrouwen"
                my_image = Image.open("assets/template_pink.png")
            else:
                categorie_text = "UNKNWON"
                my_image = Image.open("assets/template_blue.png")

            image_editable = ImageDraw.Draw(my_image)
            image_editable.text((150, 605), categorie_text, color2, font=font)

            # mainname
            naam = naam.lower()
            naam = naam.capitalize()
            nm_text = naam

            if(len(naam)>8):
                mnt = 45

            title_font = ImageFont.truetype('assets/TTOctosquaresEXP-BoldIt.ttf', mnt)  # font

            image_editable = ImageDraw.Draw(my_image)
            image_editable.text((100, 110), nm_text, color, font=title_font)

            # Id:
            id = id.lower()
            id_text = "#"+id

            image_editable = ImageDraw.Draw(my_image)
            image_editable.text((430, 110), id_text, color, font=id_font)

            # Naam:
            naam = naam.lower()
            naam = naam.capitalize()
            naam_text = naam

            image_editable = ImageDraw.Draw(my_image)
            image_editable.text((150, 275), naam_text, color2, font=font)

            # Achternaam:
            achternaam = achternaam.lower()
            achternaam = achternaam.capitalize()
            achternaam_text = achternaam
            if(len(achternaam)>10):
                a = len(achternaam)-10
                for i in range(a):
                    lstname = lstname - 5

            last_font = ImageFont.truetype('assets/TTOctosquaresEXP-BoldIt.ttf', lstname) #font

            image_editable = ImageDraw.Draw(my_image)
            image_editable.text((150, 440), achternaam_text, color2, font=last_font)

            #picture
            if(p_im!= None):
                my_image.paste(p_im,(148,712))


            resultname = id + "-" + naam + achternaam + "-" + categorie +"_kaart.png"
            my_image.save("results/kaarten/"+resultname)

def checkFields(id, naam,achternaam,categorie):
    if (id == "" or naam == "" or achternaam == "" or categorie == ""):
        return False
    else:
        return True

def imposition():
    lenFiles = len(os.listdir("results/kaarten"))
    aantalpdfs = math.ceil(lenFiles / 7)
    f = open('data.json', )
    data = json.load(f)
    index = data['indexpdf']
    f.close()

    for i in range(aantalpdfs):
        pdf = Image.open("assets/templateA4.png")
        pathlist = Path("results/kaarten").rglob('*.png')

        count = 1

        for path in pathlist:
            path_in_str = str(path)
            base = os.path.basename(path_in_str)
            if (count == 1):

                im = Image.open(path_in_str)
                im = im.rotate(90, expand=True)
                pdf.paste(im, (0, 2799))
                shutil.move(path_in_str, "results/oude-kaarten/" + base)

            elif (count == 2):
                im = Image.open(path_in_str)
                pdf.paste(im, (0, 0))
                shutil.move(path_in_str, "results/oude-kaarten/" + base)

            elif (count == 3):

                im = Image.open(path_in_str)
                pdf.paste(im, (709, 0))
                shutil.move(path_in_str, "results/oude-kaarten/" + base)

            elif (count == 4):

                im = Image.open(path_in_str)
                pdf.paste(im, (1418, 0))
                shutil.move(path_in_str, "results/oude-kaarten/" + base)

            elif (count == 5):

                im = Image.open(path_in_str)
                pdf.paste(im, (0, 1358))
                shutil.move(path_in_str, "results/oude-kaarten/" + base)

            elif (count == 6):

                im = Image.open(path_in_str)
                pdf.paste(im, (709, 1358))
                shutil.move(path_in_str, "results/oude-kaarten/" + base)

            elif (count == 7):

                im = Image.open(path_in_str)
                pdf.paste(im, (1418, 1358))
                count = 0
                shutil.move(path_in_str, "results/oude-kaarten/" + base)
                break

            count += 1
        pdf = pdf.convert('RGB')
        pdf.save("results/pdfs/" + str(index) + ".pdf")
        index += 1
        with open('data.json', 'r+') as file:
            file_data = json.load(file)
            file_data["indexpdf"] += 1
            file.seek(0)
            json.dump(file_data, file, indent=4)
