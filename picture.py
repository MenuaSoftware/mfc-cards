from PIL import Image, ImageFont, ImageDraw


class picture:
    def __init__(self,p_id,p_naam,p_achternaam,p_categorie):
        self.drawPic(p_id,p_naam,p_achternaam,p_categorie)

    def drawPic(self,id, naam,achternaam,categorie):
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
                my_image = Image.open("assets/template_rose.png")
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

            resultname = naam + achternaam + "-" + id + "-" + categorie +"_kaart.png"
            my_image.save("results/kaarten/"+resultname)
            print("id: " + id + ", Naam: " + naam + " | succesvol toegevoegd!")
        else:
            print("Something went wrong!")

def test(id, naam,achternaam,categorie):
    if (id == "" or naam == "" or achternaam == "" or categorie == ""):
        return False
    else:
        return True
