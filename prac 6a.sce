clear all;
disp("Kohonen self organizing feature map");
disp('the input pattern are')
x=[0 0 1 1;1 0 0 0;0 1 1 0;0 0 0 1]
alpha=0.5;
disp('since we have 4 input pattern and cluster unit to be formed is 2, the weight matrix is')
w=[0.2 0.9,0.4 0.7,0.6 0.5,0.8 0.3]
disp('The learning rate of this epoch is')
alpha=0.5;
i=1;
j=1;
k=1;
m=1;
while (k<=4)
    for j=1:2
        temp=0;
        for i=1:4
            temp=temp+((w(i,j)-x(k,i))^2);
        end
        D(j)=temp
    end
    if(D(1)<D(2))
        J=1;
    else
        J=2
    end
    disp('The winning unit is');
    J
    disp('weight updation');
    for m=1:4
        w(m,J)=w(m,J)+alpha*(x(k,m)-w(m,J));
    end
    w
    k=k+1
    k
end
