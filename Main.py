from PIL import Image
import numpy as np

grey="$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "

#Grey levels taken from http://paulbourke.net/dataformats/asciiart/

#these gray scales would be used in making of ascii art

print("Please Enter the path of the photo")

path=input()

im=Image.open(path).convert("L")

width=im.size[0]

height=im.size[1]

col=200#this will the default value

width_new=width/col

sc=0.43 #this works well for courier this is the default btw,source internet

height_new=width_new/sc
r=int(height/height_new)

final_im=[]


for i in range(r):
	y1=int(i*height_new)
	y2=int((i+1)*(height_new))
	if(i==r-1):
		y2=height
	final_im.append("")
	for j in range(col):
		x1=int(j*width_new);
		x2=int((j+1)*(width_new));
		if(j==col-1):
			x2=width
		imr=im.crop((x1,y1,x2,y2))
		ima=np.asarray(imr)
		w,h=ima.shape
		avg=int(np.average(ima.reshape(w*h)))
		final_im[i]+=(grey[(int((avg*69)/255))])

open("output.txt", "w").close()
file=open("output.txt",'w')
for r in final_im:
	file.write(r+'\n')
file.close()
