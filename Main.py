
from PIL import Image

grey="$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
grey10="@%#*+=-:."

#Grey levels taken from http://paulbourke.net/dataformats/asciiart/

#these gray scales would be used in making of ascii art

im=Image.open("/Users/harshit/Downloads/talia.jpg")

flip_im=im.transpose(Image.FLIP_LEFT_RIGHT)

flip_im.save("/Users/harshit/Downloads/talia_new.jpg")
