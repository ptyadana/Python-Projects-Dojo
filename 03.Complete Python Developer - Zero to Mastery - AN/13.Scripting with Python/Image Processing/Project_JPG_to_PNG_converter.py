import sys
import os
from PIL import Image
import glob

#grab first and second argugments from commad line
def main(args):
    if args:
        img_folder = args[0]
        new_img_folder = args[1]

        #check whether the folder is already existed or not, if not create a new one
        if os.path.exists(img_folder) and os.path.isdir(img_folder):
            if not (os.path.exists(new_img_folder) and os.path.isdir(new_img_folder)):
                os.mkdir(new_img_folder)
            
            convert_jpg_to_png(img_folder, new_img_folder)
        else:
            print(f'There is no {img_folder} folder. Please try again.')


def convert_jpg_to_png(img_folder, new_img_folder):
    #loop through Pokedex folder
    for file in glob.iglob(img_folder+'/*.jpg'):
        img = Image.open(file)
        file_name = img.filename.strip(img_folder)[1:].strip('.jpg')

        #convert images into PNG
        #save it to the new folder
        # img.save(new_img_folder + file_name + '.png', 'png')


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

#how to run (python name foldername newfoldername)
#python Project_JPG_to_PNG_converter.py pokedex/ pokedex/new