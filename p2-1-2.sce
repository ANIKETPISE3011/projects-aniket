disp('performed by Naghma')
a=imread('C:\Program Files\scilab-6.1.1\IPCV\images\baboon.png');
b=double(a);
subplot(1,2,1);
imshow(a);
title('Original Img');

t=100;
[m,n] = size(b);
for i =1:m
    for j = 1:n
        if(b(i,j)<t)
            c(i,j)=0;
        else
            c(i,j)=255;
        end
    end
end

subplot(1,2,2);
imshow(c);
title('Threshold Img');
