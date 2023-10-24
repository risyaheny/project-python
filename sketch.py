#libray numpy -> pip install numpy
#libray imageio -> pip install imageio
#libray scipy -> pip install scipy
#libray opencv -> pip install opencv-python
#kita pakai library image yang kemarin (pip install image)

import numpy as np
import imageio
import scipy.ndimage
import cv2

img = "gyro.jpeg" 

def rgb2gray(rgb):
    return np.dot(rgb[...,:3],[0.2989,0.5870,0.1140])
#formula untuk convert img -> graycale // 

def dodge(front,back):
    final_sketch = front*255/(255-back)
    #kalau gambarnya lebih besar dari 255 bit/px maka akan diconvert jsdi 25%
    final_sketch[final_sketch>255]=255
    final_sketch[back==255]=255

    return final_sketch.astype('uint8')

ss = imageio.imread(img)#untuk read gambar yang di pilih di awal tadi
gray = rgb2gray(ss)#untuk import gambar jadi black and white

i = 255-gray

#untuk memberi efek blur
blur= scipy.ndimage.filters.gaussian_filter(i,sigma=15)
#sigma-15 adalah insentitas blurnya

r = dodge(blur,gray)
#untuk convert gambarnya (dengan mengaplikasikan blur & black&whtie tadi)

cv2.imwrite("sketsa.png", r)
#untuk menghasilkan output gambar bernama sketsa.png
# run > start debugging
