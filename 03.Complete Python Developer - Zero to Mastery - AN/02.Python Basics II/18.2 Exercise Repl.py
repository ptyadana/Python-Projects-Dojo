#Exercise!
#Display the image below to the right hand side where the 0 is going to be ' ', 
# and the 1 is going to be '*'. This will reveal an image!
picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

#version 1
# for y_list in picture:
#     row_image = ""
#     for x in y_list:
#         if x:
#            row_image += "*"
#         else:
#             row_image += " "
#     print(row_image)

#version 2
fill = "*"
space = " "
empty = ""
for row in picture:
    for pixel in row:
        if pixel:
            #overwrite the end to "" instead of new line for print function
            print(fill, end=empty)
        else:
            print(space, end=empty)
    #new line after each row
    print(empty) 