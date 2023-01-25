X= [1,1], [1,-1], [-1,1] , [-1,-1]
print('inputs=')
for x in X:
    print(x)
Y=[1,-1,-1, -1]
print('target=',Y)
w=[0,0]
print('initial weight values=',w)
for i in range(len(X)):
    for j in range(len(w)):
        w[j]=w[j]+X[i][j] *Y[i]
    print(i,'iteration weight values=',w)
