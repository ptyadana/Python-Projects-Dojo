from PIL import Image, ImageFilter

img = Image.open('./astro/astro.jpg')
print(img.size)

#keep aspect ratio
img.thumbnail((400,400))
img.save('./astro/processed/thumbnail.jpg')

print(img.size)