from PIL import Image
import sys

def parse(path):
    img=Image.open(path)
    h,w=img.size
    
    px=img.load()
    for i in range(h):
        for j in range(w):
            R,G,B=px[i,j]
            R=R//2
            G=G//2
            B=B//2
            px[i,j]=(R,G,B)
    img.save('Q2.jpg')

if __name__== "__main__":
    parse(sys.argv[1])

