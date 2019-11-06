
#%%
from PIL import Image, ImageDraw
 
img = Image.new('RGB', (200, 200), color = ('pink'))
 
d = ImageDraw.Draw(img)
d.text((50,50), "Sthephany", fill=('black'))
 
img

#%%
 from PIL import Image, ImageFilter 
 
 img = Image.new('RGB', (200, 200), color = ('pink'))
 img.new(ImageFilter.GaussianBlur(15)).save

 img 

###Trying to make the image blur but isnt working. https://stackoverflow.com/questions/21215903/blurring-an-image-using-pil-in-python

#%%
from PIL import Image

img = Image.open ("Free-projects/beach1.jpg")
img 

#%%
from PIL import Image

img = Image.open ("Free-projects/beach1.jpg")
img.rotate(180).show()

