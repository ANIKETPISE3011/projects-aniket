
num=int(input('Enter the number of inputs'))
w1=1#assume both weightsare excitatory
w2=1
print('for the ',num,'inputs calculayte he net input')
x1=[]
x2=[]
for i in range (0,num):
    ele1=int(input('x1='))
    ele2=int(input('x2='))
    x1.append(ele1)
    x2.append(ele2)
print('x1=',x1)
print('x2=',x2)
n=[w1* i for i in x1]
m=[w2* i for i in x2]
Yin=[]
for i in range(0,num):
    Yin.append(n[i]+m[i])
print('\nExcitatory weight')
print('Yin=',Yin)
#assume one weight as excitatory and inhibititory
w1=1
w2=-1
n=[w1*i for i in x1]
m=[w2*i for i in x2]
Yin=[]
for i in range(0,num):
    Yin.append(n[i]+m[i])
print('\n inhibititory weight')
print('Yin=',Yin)
print('\n After assuming one weight as exitatory and one as inhibititory,')
Y=[]
for i in range(0,num):
    if(Yin[i]>=1):
        ele1=1
        Y.append(ele)
    if (Yin[i]<1):
        ele=0
        Y.append(ele)
print('Y=',Y)
