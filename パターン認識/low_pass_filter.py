import numpy as np
from PIL import Image
im  = np.array(Image.open('input.png').convert('L'))
f_im = np.fft.fft2(im)
h, w = im.shape
center_y, center_x =  int(h/2), int(w/2)
flt=0.8
flt_h, flt_w = int(flt*center_y), int(flt*center_x)
shift_f_im =  np.fft.fftshift(f_im)
zero_im = np.zeros(im.shape, dtype=complex)
shift_f_im[center_y-flt_h:center_y+flt_h, center_x-flt_w:center_x+flt_w]\
        = zero_im[center_y-flt_h:center_y+flt_h, center_x-flt_w:center_x+flt_w]
shift_f_im =  np.fft.fftshift(shift_f_im)
if_im = np.fft.ifft2(shift_f_im)
if_im_real = np.uint8(if_im.real)
Image.fromarray(if_im_real).save('output.png')
