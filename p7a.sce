 clear;
 clc;
 I=imread('C:\Program Files\scilab-6.1.1\IPCV\images\morpex.png')
 subplot(2,3,1)
 imshow(I)
 title("Original Image by Aniket & Pratim")
 se=imcreatese('rect',3,3)
 erode=imerode(I,se);
 subplot(2,3,2)
 imshow(erode)
 title("Eroded Image")
 
 dilate=imdilate(I,se)
 subplot(2,3,3)
 imshow(dilate)
 title("dilated Iamge")
 
open=imopen(I,se)
subplot(2,3,4)
imshow(open)
title("Open Image")

closed=imclose(I,se)
subplot(2,3,5);imshow(closed)
title("Closed Image")
  
                                        
