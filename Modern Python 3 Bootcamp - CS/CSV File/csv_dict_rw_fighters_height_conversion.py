import os.path
from csv import DictWriter,DictReader

#convert cm to inches
def cm_to_in(cm):
    return cm * 0.393701

#read file
with open('fighters.csv') as file: 
    csv_reader = DictReader(file)
    
    #skip over header
    next(csv_reader,None)
    fighters = list(csv_reader)

#prepare to write file
#for python 3: use newline='', otherwise the file will have extra line between the wrttien rows
with open('heightconverted_fighters.csv','w',newline='') as f:
    new_headers = ['Name','Country','Heights (in inches)']
    csv_writer = DictWriter(f,fieldnames=new_headers)
    csv_writer.writeheader()

    #read the content of original file and write to new one
    for f in fighters:
        fighter_height_inches = cm_to_in(float(f['Height (in cm)']))
        csv_writer.writerow({
            'Name':f['Name'],
            'Country':f['Country'],
            'Heights (in inches)':fighter_height_inches
        })




