clear
clc
a=imread('C:\Program Files\scilab-6.1.1\IPCV\images\morpex.png')
se=imcreatese('ellipse',3,3)

erosion=imerode(a,se)
Boundary=a-erosion

subplot(2,2,1);imshow(a);title('Original Image by Aniket & pratim')

subplot(2,2,2);imshow(erosion);title('Eroded Image')

subplot(2,2,3);imshow(Boundary);title('Boundary Image')
