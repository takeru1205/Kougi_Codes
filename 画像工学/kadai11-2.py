from PIL import Image
import matplotlib, sys
import matplotlib.pyplot as plt
import numpy as np
img = Image.open(sys.argv[1]+'.pgm')
width, height = img.size
hist = [0,]*256
for j in range(height):
    for i in range(width):
        pixval = img.getpixel((i, j))
        hist[pixval] += 1
rate = 0.81
th = sum(hist) * rate
sum = 0
for i in range(256):
    sum += hist[i]
    if sum > th:
        th = i
        break
for j in range(height):
    for i in range(width):
        if img.getpixel((i, j)) > th:
            img.putpixel((i, j), 255)
        else:
            img.putpixel((i,j),0)


imgArray = np.asarray(img)
imgArray.flags.writeable = True
imgArray[imgArray==255]=1

def check(array, x, y, look_up_table):
    check_list = []
    try:
        if array[y-1][x-1] != 0:
            check_list.append(array[y-1][x-1])
    except:
        pass
    try:
        if array[y-1][x] != 0:
            check_list.append(array[y-1][x])
    except:
        pass
    try:
        if array[y-1][x+1] != 0:
            check_list.append(array[y-1][x+1])
    except:
        pass
    try:
        if array[y][x-1] != 0:
            check_list.append(array[y][x-1])
    except:
        pass
    if len(check_list) == 0:
        return 0, look_up_table
    else:
        if len(check_list) > 1:
            for i in check_list:
                look_up_table[i][1] = min(check_list)
        return min(check_list), look_up_table

def labeling(array):
    lastnum = 1 # 初期値
    print(array.shape)
    height, width = array.shape
    # ルックアップテーブルの作成
    size = (width/2+width%2)*(height/2+height%2)
    look_up_table = np.array([i for i in range(int(size))])
    look_up_table = np.c_[look_up_table, look_up_table]
    print(look_up_table.shape)
    for i in range(height):
        for j in range(width):
            if array[i, j]==1:
                check_num, look_up_table = check(array, j, i, look_up_table)
                if check_num == 0:
                    lastnum += 1
                else:
                    array[i,j] = lastnum
    for i in look_up_table:
        if i[0] == i[1]:
            pass
        else:
            array[array==i[0]]=i[1]
    return np.amax(array)

print(labeling(imgArray))
