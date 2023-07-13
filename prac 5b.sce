clc;
clear;
disp('Aniket & Pratim')
Image=imread('C:\Program Files\scilab-6.1.1\IPCV\images\balloons.png')
subplot(1,3,1);imshow(Image);title('Image in RGB color space')
HSV=rgb2hsv(Image);
subplot(1,3,2);imshow(HSV);title('Image in HSV color Space')
CMY=imcomplement(Image);
subplot(1,3,3);imshow(CMY);title('Image in CMY Space')
