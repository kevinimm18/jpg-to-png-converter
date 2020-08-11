import sys
import os
from PIL import Image

#Grab first and second argument
image_folder = sys.argv[1]
output_folder = sys.argv[2]

#Check if new atau exist. If not, create it
if not os.path.exists(output_folder):
	os.makedirs(output_folder)

#Loop through Folder Pokedex
for filename in os.listdir(image_folder):
	img = Image.open(f'{image_folder}{filename}')
	clean_name = os.path.splitext(filename)[0]

#Convert images to PNG dan Save to the new folder
	img.save(f'{output_folder}{clean_name}.png', 'png')
	print('All done !')
