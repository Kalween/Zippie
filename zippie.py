import os
from zipfile import ZipFile
import time

katalog = "[folder name]"
filformat = ".zip"

os.chdir(katalog)
print(os.getcwd())

# while True:
#     time.sleep(60)
for item in os.listdir(katalog): #Loopa igenom alla filer i katalogen
    if item.endswith(filformat): #Kolla efter zipfiler
        path_name = os.path.abspath(item) #Hämta fulla namnet på filen
        file_name = os.path.basename(path_name)
        print(file_name)
        zip_ref = ZipFile(path_name) #Skapa zipfil object
        with ZipFile(file_name) as zipObj:
            listOffiles = zipObj.namelist()
        zip_ref.extractall(katalog) #Unzip alla i katalog2       
        zip_ref.close()  # Stäng filen
        os.rename(listOffiles[0], file_name[:-4]+'.Html')
        os.remove(file_name) #Ta bort zipfilen