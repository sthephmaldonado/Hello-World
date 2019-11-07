Excercise 10_2 
#%%
from PIL import Image

im = Image.open("Exercises for Reflections/Taj.jpg")

im = im.rotate(180)

img.show()

im.save("Exercises for Reflections/Taj_vertically.jpg")