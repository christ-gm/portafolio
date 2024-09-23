import os
import shutil

user = os.getlogin() #Get current user

origin = f"/home/{user}/Datasets/Acrima_Database/Images" #Set acrima dataset location
destiny = "./acrimaDataset/" #Destiny location of dataset

os.makedirs(name=destiny, exist_ok=True) #Create dataset directory
os.makedirs(name=os.path.join(destiny, "glaucoma"), exist_ok=True)
os.makedirs(name=os.path.join(destiny, "normal"), exist_ok=True)

img_names = os.listdir(origin) #Get names of images

for im in img_names:
    origin_path = os.path.join(origin, im) #Get path of each original image
    if ('_g_' in im):
        shutil.copy(origin_path, os.path.join(destiny, "glaucoma", im))
    else:
        shutil.copy(origin_path, os.path.join(destiny, "normal", im))
