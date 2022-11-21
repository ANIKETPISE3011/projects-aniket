import math
n=int(input('enter number of input neurons:'))
print('enter the input')
inputs=[]
for i in range (0,n):
    x= float(input())
    inputs.append(x)
print('inputs')
print('enter the weights')
weights=[]
for i in  range(0,n):
    w=float(input())
    weights.append(w)
print('weights')
print('the net inputs by using Yin= x1w1 + x2w2 + x3w3')
Yin=[]
for i in range (0,n):
      Yin.append(inputs[i]*weights[i])
ynet = round(sum(Yin),3)
print('net inputs for y neurons=',ynet)
print('apply activation funstion over net inputs, A) binary sigmodial activation function')
y = round(1/(1+math.exp(-ynet)),3)
print(y)
print('apply activation funstion over net input, B) bipolar sigmoidal activation function')
y = round(2/(1+math.exp(-ynet))-1,3)
print(y)
