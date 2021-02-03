import PIL as pl
from PIL import Image
from colr import color as C
import cv2
import os
import time
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
		#print("                ",end="")
		self.img = ""
		for i in range(len(pixels)):
			self.img += C(self.chr[(sum(pixels[i])//3)//self.ln],fore=pixels[i])
			if (i+1)%self.nw == 0:
				self.img+='\n'
		print(self.img)
	def to_ascii(self):
		Picture.shrink(self)
		Picture.p2a(self)
	

class Video():
	def __init__(self,width=110):
		self.nw = width
		self.chr = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']#["@", "#", "$", "%", "?", "*", "+", ";", ":","-", ",", "."]#["@", "#","$","S", "%", "?", "*","^", "+","!",";", ":", ",", "."]
		self.ln = (256+len(self.chr))//len(self.chr)
		vid = cv2.VideoCapture(0)
		ret,self.frame = vid.read()
		vid.release()
		w,h,c = self.frame.shape
		r = w/h/1.65
		self.nh = int(self.nw*r)
		self.x = len(self.frame)
		self.y = len(self.frame[0])
	def show(self):
		self.img = ""
		for i in range(len(self.frame)):
			for j in range(len(self.frame[0])):
				self.img += C(self.chr[(sum(self.frame[i][j])//3)//self.ln],fore=(self.frame[i][j][2],self.frame[i][j][1],self.frame[i][j][0]))
			self.img+='\n'
		os.system('clear')
		print(self.img)
	def to_vid(self):
		vid = cv2.VideoCapture(0)
		while True:
			ret,self.frame = vid.read()
			self.frame = cv2.flip(cv2.resize(self.frame, (self.nw, self.nh)), 1) 
			Video.show(self)
			if cv2.waitKey(1) == 27:
				vid.release()
				break