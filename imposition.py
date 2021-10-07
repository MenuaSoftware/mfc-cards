import os, os.path
import math
import json
from pathlib import Path
from PIL import Image, ImageDraw
import shutil


class imposition:
    def __init__(self):
        lenFiles = len(os.listdir("results/kaarten"))
        aantalpdfs = math.ceil(lenFiles/7)
        f = open('data.json', )
        data = json.load(f)
        index = data['indexpdf']
        f.close()
        print("aantal bestanden: " + str(lenFiles))
        print("aantal pdfs: " + str(aantalpdfs))
        print("start index van pdf is: " + str(index))

        for i in range(aantalpdfs):
            pdf = Image.open("assets/templateA4.png")
            pathlist = Path("results/kaarten").rglob('*.png')

            count = 1

            for path in pathlist:
                path_in_str = str(path)
                base = os.path.basename(path_in_str)
                print("------------------")
                if(count == 1):
                    print("1")
                    print(path_in_str)
                    print("base: " + base)

                    im = Image.open(path_in_str)
                    im = im.rotate(90,expand=True)
                    pdf.paste(im,(0,2799))
                    shutil.move(path_in_str,"results/oude-kaarten/"+base)

                elif(count == 2):
                    print("2")
                    print(path_in_str)
                    print("base: " + base)

                    im = Image.open(path_in_str)
                    pdf.paste(im,(0,0))
                    shutil.move(path_in_str,"results/oude-kaarten/"+base)

                elif(count == 3):
                    print("3")
                    print(path_in_str)
                    print("base: " + base)

                    im = Image.open(path_in_str)
                    pdf.paste(im,(709,0))
                    shutil.move(path_in_str,"results/oude-kaarten/"+base)

                elif(count == 4):
                    print("4")
                    print(path_in_str)
                    print("base: " + base)

                    im = Image.open(path_in_str)
                    pdf.paste(im,(1418,0))
                    shutil.move(path_in_str,"results/oude-kaarten/"+base)

                elif(count == 5):
                    print("5")
                    print(path_in_str)
                    print("base: " + base)

                    im = Image.open(path_in_str)
                    pdf.paste(im,(0,1358))
                    shutil.move(path_in_str,"results/oude-kaarten/"+base)

                elif(count == 6):
                    print("6")
                    print(path_in_str)
                    print("base: " + base)

                    im = Image.open(path_in_str)
                    pdf.paste(im,(709,1358))
                    shutil.move(path_in_str,"results/oude-kaarten/"+base)

                elif(count == 7):
                    print("7")
                    print(path_in_str)
                    print("base: " + base)

                    im = Image.open(path_in_str)
                    pdf.paste(im,(1418,1358))
                    count = 0
                    shutil.move(path_in_str,"results/oude-kaarten/"+base)
                    break

                count += 1
            pdf = pdf.convert('RGB')
            pdf.save("results/pdfs/" + str(index) + ".pdf")
            print("SAVED")
            index +=1
            with open('data.json', 'r+') as file:
                file_data = json.load(file)
                file_data["indexpdf"] += 1
                file.seek(0)
                json.dump(file_data, file, indent=4)







if __name__ == '__main__':
    imposition()