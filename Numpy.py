"""numpy is the core libraray for scientific computing.it provides a high 
performance multi dimensional array object and tools for working on those arrays."""

import numpy as np
a=np.array([1,2,3])
print(a)

import numpy as np
my_mat = [[1,2,3],[4,5,6],[7,8,9]]
np.array(my_mat)
print(my_mat)

import numpy as np
b=np.array([(1.0,2,3),(4,5,6)])
print (b.itemsize)


import numpy as np
b=np.array([(1,2,3),(4,5,6)])
print(b.size)


import numpy as np
b=np.array([(1,2,3),(4,5,6)])
print(b.shape)

import numpy as np
b=np.array([(1,2,3),(4,5,6)])
print(b)

b=b.reshape(3,2)
print (b)

#Line space - values 1 and 10

import numpy as np
b=np.linspace(1,10,4)
print (b)

#Max/min value in an array

import numpy as np
b=np.array([(1,2,3),(4,5,6)])
print(b.max())

#sum of elements of array

import numpy as np
b=np.array([(1,2,3),(4,5,6)])
print(b.sum())

#sum of elements in each column(axis=0)

import numpy as np
b=np.array([(1,2,3),(4,5,6)])
print(b.sum(axis=0))

#sum of elements in each row(axis=1)

import numpy as np
b=np.array([(1,2,3),(4,5,6)])
print(b.sum(axis=1))

#square root of each element in array

import numpy as np
b=np.array([(1,2,3),(4,5,6)])
print(np.sqrt(b))

#standard deviation 

import numpy as np
b=np.array([(1,2,3),(4,5,6)])
print(np.std(b))

#sum of two arrays

import numpy as np
b=np.array([(1,2,3),(4,5,6)])
c=np.array([(1,2,3),(4,5,6)])
print(b+c)

#vertical stacking
import numpy as np
b=np.array([(1,2,3),(4,5,6)])
c=np.array([(1,2,3),(4,5,6)])
print(np.vstack((b,c)))

#horizontal stacking
import numpy as np
b=np.array([(1,2,3),(4,5,6)])
c=np.array([(1,2,3),(4,5,6)])
print(np.hstack((b,c)))

#multi array into 1d

import numpy as np
b=np.array([(1,2,3),(4,5,6)])
print (np.ravel(b))


#Function arange

import numpy as np
import matplotlib.pyplot as plt
x=np.arange(0,np.pi,0.1)
y=np.cos(x)
plt.plot(x,y)
plt.show()