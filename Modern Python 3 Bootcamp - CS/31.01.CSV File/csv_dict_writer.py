from csv import writer,DictWriter
import os.path

# #using writer
# with open('cats.csv','w') as file:
#     csv_writer = writer(file)
#     csv_writer.writerow(['Name','Breed','Age'])
#     csv_writer.writerow(['Lion','Mixed','2'])

#using DictWriter
file_name = os.path.join('./files/','cats.csv')
with open(file_name,'w', newline='') as file:
    headers = ['Name','Breed','Age']
    csv_dict_writer = DictWriter(file,fieldnames=headers)
    csv_dict_writer.writeheader()
    csv_dict_writer.writerow({
        'Name':'Conny',
        'Breed':'Burmese Shorthair',
        'Age':'5'
    })
    