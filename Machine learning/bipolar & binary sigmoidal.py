import math
n= int(input('enter number of input number: ='))
print('Enter the input')
inputs=[]

for i in range (0,n):
    x=float(input())
    inputs.append(x)
print(inputs)

print('Enter the weights')
weights = []
for i in range(0,n):
    w= float(input())
    weights.append(w)

print(weights)

print('The net input can be calculated as Yin = x1w1 + x2w2 +x3w3')

Yin= []
for i in range(0,n):
    Yin.append(inputs[i]*weights[i])
ynet= round(sum(Yin), 3)

print('Net inputs for y neurons= ', ynet)
print('Apply activation function over net input, A) Binary sigmoidal activation function')
y= round(1/(1+math.exp(-ynet)),3)
print(y)

print('Apply activation function over net  input, B) Biploar sigmoidal activation function')
y=round(2/(1+math.exp(-ynet))-1,3)

print(y)
