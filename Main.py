
from PIL import Image

grey="$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
grey10="@%#*+=-:."

#Grey levels taken from http://paulbourke.net/dataformats/asciiart/

#these gray scales would be used in making of ascii art

print("Please Enter the path of the photo")

path=input()

im=Image.open(path).convert("L")

im.show()



