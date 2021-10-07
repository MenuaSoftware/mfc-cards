import os, os.path
import math
class imposition:
    def __init__(self):
        lenFiles = len(os.listdir("results/kaarten"))
        aantalpdfs = math.ceil(lenFiles/7)
        print("aantal bestanden: " + lenFiles)
        print("aantal pdfs: " + aantalpdfs)




if __name__ == '__main__':
    imposition()