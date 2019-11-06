[Free Project 11-1] Image Manipulation as You Like It
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

#%%
from PIL import Image, ImageFilter

img = Image.open ("Free-projects/beach1.jpg")
img = img.filter(ImageFilter.GaussianBlur(radius = 5)) 
  
img.show()  

#%%
from PIL import Image

img = Image.open("Free-projects/beach1.jpg")
gray = col.convert('L')
bw = gray.point(lambda x: 0 if x<128 else 255, '1')
bw.save("result_bw.png")
img.show()

##I tried making the image black and white but it didnt worked. The picture just become all black
https://stackoverflow.com/questions/18777873/convert-rgb-to-black-or-white?rq=1