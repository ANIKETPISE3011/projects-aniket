num_ip=int(input('Enter the number of inputs'))
w1=1#assume both weights are excitatory
w2=1
print('for the ',num_ip,'inputs calculate the net input')
x1=[]
x2=[]
for  i in range (0,num_ip):
    ele1=int(input('x1='))
    ele2=int(input('x2='))
    x1.append(ele1)
    x2.append(ele2)

print('x1=',x1)
print('x2=',x2)
n= [w1* i for i in x1]
m= [w2* i for i in x2]
Yin=[]
for i in range(0,num_ip):
    Yin.append(n[i]+m[i])
print('\n Excitatory weights')
print('Yin',Yin)
#Assume one weight as excitatory and one as inhibitatory
w1=1
w2=-1
n=[ w1* i for i in x1]
m=[w2* i for i in x2]
Yin= []
for i in range (0, num_ip):
    Yin.append(n[i]+m[i])
print('\n inhibitatory weights')
print('Yin',Yin)
print('\n After assuming one weights as exhibitatory and one as inhibitory')
Y=[]
for i in range(0,num_ip):
    if(Yin[i]>=1):
        ele=1
        Y.append(ele)
    if(Yin[i]<1):
        ele=0
        Y.append(ele)
print('Y',Y)
             
