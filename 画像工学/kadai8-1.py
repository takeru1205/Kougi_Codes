from PIL import Image
import matplotlib, sys
#matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
img = Image.open(sys.argv[1]+'.pgm')
width, height = img.size
hist = [0,]*256
for j in range(height):
    for i in range(width):
        pixval = img.getpixel((i, j))
        hist[pixval] += 1

rate = 0.7


th = sum(hist) * rate

sum = 0
for i in range(256):
    sum += hist[i]
    if sum > th:
        th = i
        break

print(th)

for j in range(height):
    for i in range(width):
        if img.getpixel((i, j)) > th:
            img.putpixel((i, j), 255)
        else:
            img.putpixel((i,j),0)

#img.show()
img.save(sys.argv[1]+'.png')
#plt.savefig(sys.argv[2]+'.png')
plt.plot(hist)
plt.plot([th, th], [0, max(hist)], 'r-', linewidth=1.0)
plt.show()
