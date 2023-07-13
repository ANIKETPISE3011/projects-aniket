clc
clear
disp('naghma')
a=imread('C:\Program Files\scilab-6.1.1\IPCV\images\balloons.png')

Image=rgb2gray(a)

NoisyImage=imnoise(Image,'salt & pepper')
Output=immedian(NoisyImage,[3,3])

subplot(1,3,1)
imshow(Image)
title('Original Image')

subplot(1,3,2)
imshow(NoisyImage)
title('Noisy Iamge')

subplot(1,3,3)
imshow(Output)
title('Filtered Image')
