clear;
clc;
a=imread('C:\Program Files\scilab-6.1.1\IPCV\images\lena7030.bmp')
se=imcreatese('ellipse',10,10)

opening=imopen(a,se)
Top_hat=a-opening

closed=imopen(a,se)
Bottom_Hat=closed-a

subplot(2,3,1);imshow(a);title('Original Image by Aniket & Pratim')
subplot(2,3,2);imshow(opening);title('Opening Image')
subplot(2,3,3);imshow(Top_hat);title('Top_Hat image')
subplot(2,3,4);imshow(closed);title('Closed Image')
subplot(2,3,5);imshow(Bottom_Hat);title('Bottom_Hat Image')
