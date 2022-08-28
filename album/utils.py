import math
from PIL import Image

def thumbnail(img, size):
	w1, h1 = img.size
	w2, h2 = size
	r = min(float(w2)/float(w1), float(h2)/float(h1))	
	scale = (int(math.ceil(w1*r)), int(math.ceil(h1*r)))
	img.thumbnail(scale, Image.ANTIALIAS)	
	return img

def crop_thumbnail(img, size):
	w1, h1 = img.size
	w2, h2 = size
	r = max(float(w2)/float(w1), float(h2)/float(h1))	
	scale = (int(math.ceil(w1*r)), int(math.ceil(h1*r)))
	img.thumbnail(scale, Image.ANTIALIAS)	

	box = (0, 0, int(w2), int(h2))
	img = img.crop(box)
	#img = img.crop((0, 0, int(w2), int(h2)))
	print box, img.size
	return img

