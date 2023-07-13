clc;
clear;
disp('Performed by Naghma')
a=imread('C:\Program Files\scilab-6.1.1\IPCV\images\cameraman.tif')
a=im2double(a);
subplot(2,3,1)
imshow(a)
title('Input Image')
[m,n]=size(a);
D0 =50;
A=fft2(a);
subplot(2,3,2)
imshow(uint8(abs(A)))
title('F.T of i/p without shift');
A_shift=fftshift(A);
A_real=abs(A_shift);
subplot(2,3,3)
imshow(uint8(A_real))
title('F T  of i/p after shift');
A_low=zeros(m,n);
d=zeros(m,n);
for u=1:m
    for v=1:n
        d(u,v)=sqrt((u-(m/2))^2+(v-(n/2))^2);
        if d(u,v)<=D0
            A_low(u,v)=A_shift(u,v);
            filt(u,v)=1;
        else
            A_low(u,v)=0;
            filt(u,v)=0;
        end
    end
end
subplot(2,3,4),imshow(filt),title('Ideal Low Pass Filter')
subplot(2,3,5),mesh(filt),title('surface plot LPF')
B=fftshift(A_low);
B_inverse=ifft(B);
B_real=abs(B_inverse);
subplot(2,3,6),imshow(B_real),title('Low pass Image')
