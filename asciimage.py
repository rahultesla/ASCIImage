import PIL as pl
from PIL import Image
from colr import color as C
class Picture():
	def __init__(self,path,width=98):
		self.image = Image.open(path)
		self.nw = width
		self.chr = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']#["@", "#", "$", "%", "?", "*", "+", ";", ":","-", ",", "."]#["@", "#","$","S", "%", "?", "*","^", "+","!",";", ":", ",", "."]
		self.ln = (256+len(self.chr))//len(self.chr)
	def shrink(self):
		w,h = self.image.size
		r = w/h/1.65
		self.nh = int(self.nw*r)
		self.image = self.image.resize((self.nw,self.nh))
	def p2a(self):
		pixels = self.image.getdata()
		print("                ",end="")
		for i in range(len(pixels)):
			try:
				print(C(self.chr[(sum(pixels[i])//3)//self.ln],fore=pixels[i]),end="")
			except:
				print((sum(pixels[i])//3)//self.ln)
				break
			if (i+1)%self.nw == 0:
				print("")
				print("                ",end="")
	def to_ascii(self):
		Picture.shrink(self)
		Picture.p2a(self)
