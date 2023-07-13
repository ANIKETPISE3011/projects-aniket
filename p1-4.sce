disp('performed by Naghma')
a=imread('C:\Program Files\scilab-6.1.1\IPCV\images\Lena_dark.png');
b=imnoise(a,'gaussian')
imshow(b)
imwrite(b,'gaussian.jpg')
