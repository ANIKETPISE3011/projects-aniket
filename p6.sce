clc;
clear;
a=imread('C:\Program Files\scilab-6.1.1\IPCV\images\measure_gray.jpg')
dctImg=imdct(a)
subplot(1,2,1)
imshow(a)
title('Original Image by Aniket & Pratim')
subplot(1,2,2)
imshow(dctImg,rainbowcolormap(32));
title('Discrete Cosine Transform')
