from PIL import Image
import matplotlib, sys
matplotlib.use('Agg')
import matplotlib.pyplot as plt
img = Image.open(sys.argv[1]+'.pgm')
width, height = img.size
hist = [0,]*256
for j in range(height):
    for i in range(width):
        pixval = img.getpixel((i, j))
        hist[pixval] += 1

plt.plot(hist)
plt.savefig(sys.argv[2]+'.png')
