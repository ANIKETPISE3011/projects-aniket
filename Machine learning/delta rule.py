import numpy as np
import time
np.set_printoptions(precision=9)
x=np.zeros((3,))
weights= np.zeros((3,))
desired=np.zeros((3,))
actual= np.zeros((3,))
for i in range(0,3):
    x[i]=float(input('initial inputs=',))
for i in range(0,3):
    weights[i]=float(input('initial weights=',))
for i in range(0,3):
    desired[i]=float(input('desired weights=',))
for i in range(0,3):
    actual=x[i]*weights
print('actual:',actual)
print('desired:',desired)
a=float(input('Enter learning rate:'))
while True:
    if np.array_equal(desired, actual):
        break #no change
    else:
        for i in range(0,3):
            weights[i]=weights[i]+a*(desired[i]-actual[i])
            actual=x[i]*weights
    print('weights',weights)
    print('actual',actual)
    print('desired',desired)

print('Final output')
print('CCorrected weights',weights)
print('actual',actual)
print('desired',desired)
