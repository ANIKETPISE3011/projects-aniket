x=int(input('Enter the value of x'))
b=int(input('Enter the value of bais'))
w=int(input('Enter the value of weight'))
ynet=w*x+b
print('net input for y neuron =',ynet)
print('apply activation function over net input , ramp function')
if ynet <0:
    output= 0
elif ynet >=0 and ynet<=1:
    output =ynet
else:
    output=1
print('output=',output)
