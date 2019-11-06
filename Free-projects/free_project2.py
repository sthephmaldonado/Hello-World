#%%
from PIL import Image
 
img = Image.new('RGB', (60, 30), color = 'blue')

img

#%%
from PIL import Image, ImageDraw
 
img = Image.new('RGB', (100, 60), color = ('pink'))
 
d = ImageDraw.Draw(img)
d.text((10,10), "Sthephany", fill=(255,255,0))
 
img.save('pil_text.png')

img
