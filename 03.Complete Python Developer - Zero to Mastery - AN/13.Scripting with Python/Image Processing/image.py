from PIL import Image, ImageFilter

img = Image.open('./pokedex/squirtle.jpg')

print(img.format)
print(img.size)
print(img.mode)

#display all the things that img is given to use
# print(dir(img))

#convert as blur
filtered_img = img.filter(ImageFilter.BLUR)
filtered_img.save('./pokedex/processed/blurred_squ.png','png')

#convert to greyscale
filtered_img2 = img.convert('L')
filtered_img2.save('./pokedex/processed/greyscale_squ.png', 'png')
# filtered_img2.show()

#crop
box = (100,100,400,400)
region = filtered_img2.crop(box)
region.save('./pokedex/processed/cropped_squ.png', 'png')
region.show()

crooked_img = img.rotate(90)
crooked_img.save('./pokedex/processed/crooked_squ.png', 'png')

small_img = img.resize((100,100))
small_img.save('./pokedex/processed/small_squ.png', 'png')



