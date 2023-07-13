clc
clear
disp('Naghma')
Image=imread('C:\Program Files\scilab-6.1.1\IPCV\images\balloons.png')

NoisyImage=imnoise(Image,'gaussian',0.02)

wienerfilter=imwiener2(NoisyImage,[5,5],0.2)

subplot(1,3,1)
imshow(Image)
title('Original Image')

subplot(1,3,2)
imshow(NoisyImage)
title('Noisy Image')

subplot(1,3,3)
imshow(wienerfilter)
title('Filtered Image')
