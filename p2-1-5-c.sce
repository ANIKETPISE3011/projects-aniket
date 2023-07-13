clc;
clear ;
disp('Naghma')
a = imread('C:\Program Files\scilab-6.0.0\IPCV\images\lena.png');
b=double(a);

for i=1:8
    f=bitget(b,i)
    subplot(2,4,i);
    imshow(f);
    title('bit plane'+string(i));
end
