clear all;
function [yin,y]=net(j,w,x,temp,theta,yin,y)
    yin=yin
    y=y
    for i=1:4
        temp=temp+(y(i)*w(i,j));
    end
    yin(j)=x1(j)+temp;
    if(yin(j)>theta)
        y(j)=1;
    elseif(yin(j)==theta)
        y(j)=yin(j);
    else
        y(j)=-1
    end
    disp(yin)
    disp(y)
endfunction
disp("Discreate Hopfiled Network");
theta=0;
x=[1 1 1 -1]
w=x'*x
disp("weight mattrix with self connection")
disp(w);
for i=1:4
    for j=1:4
        if(i==j)
            w(i,j)=0
end
end
end
disp("weight matrix with no self connection");
disp(w);
disp("Given input for testing");
x1=[1 1 1 -1]
y=[1 1 1 -1]
temp=0;
disp("by asynchroonous updation method");
disp("the net input calculated is");
yin=[0 0 0 0 ]
[yin,y]=net(1,w,temp,theta,yin,y)
[yin,y]=net(4,w,temp,theta,yin,y)
[yin,y]=net(3,w,temp,theta,yin,y)
[yin,y]=net(2,w,temp,theta,yin,y)
disp("the output calculated fromnet input is")
disp(y)
