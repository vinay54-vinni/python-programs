# numpy:
# num = numeric ,py = Python
# for doing faster numeric calculations we use numpy or for working with numbers we use numpy
#NumPy's default data type for numerical arrays populated with zeros, empty spaces, or generated ranges is a float
#question : we can also do this calculations using modules in python then why we want to use this numpy 
#ans:The short answer is Speed and Memory.
# While plain Python can do all of these calculations using built-in lists and loops,
# it becomes painfully slow and inefficient when working with large amounts of data (like images, which have thousands of pixels, or machine learning datasets with millions of rows).
# example:

# import numpy as np
# np.zeros(3)
# if we use this we can't able to print an output but same code print the output in jupter notebook cause
# In Jupyter Notebooks: Jupyter runs on an interactive execution model. The very last line of code in any cell is automatically evaluated and displayed as an output cell below it (known as REPL or Read-Eval-Print Loop behavior).
# Because np.zeros(3) returns the array object, Jupyter automatically prints it for you without needing the word print


import numpy as np
z = np.zeros(3)
print(z)
type(z[0])#output:[0. 0. 0.]
#if we print we get output in array with datatype float automatically. but if we want that in integer you can explicitly specify the data type by passing the dtype=int argument


import numpy as np
z = np.zeros(3,dtype=int)#zeros is used for getting zeros ,3 means how many times we want to print that 0 here we are printing 3 times
print(z)#output:[0 0 0]

a = np.ones(5)#like zeros like ones
print(a)#output:[1. 1. 1. 1. 1.]


b = np.linspace(2,10,5)#linspace is used to get elemts between like here we are giving that we want output from 2 to 10 and 5 indicates how many numbers we want between that 
print(b)#output:[ 2.  4.  6.  8. 10.]
#we can also do slicing here in numpy

np.random.seed(54)
array_1 = np.random.randint(10,size=6)#we use this to print some random numbers between 1 to 10 with sizw 5 if we dosen't give any saarting number it means it start with 1
print(array_1)
np.random.seed(54)
array_2 = np.random.randint(10,size=6)
print(array_2)

#from array_1 &2 if we want to get same random elements if we want to use random.seed()


#if we want to display a photo or want to know the size of the photo we use this 

from skimage import io
photo = io.imread("photo.png")
print(photo.shape)

import matplotlib.pyplot as plt
plt.imshow(photo)#it print normal photo
plt.show()

plt .imshow(photo[::-1])#it prints the reversed image 
plt.show()

plt .imshow(photo[:,::-1])#it prints the reversed image 
plt.show()#it prints the photo column reverse 

plt .imshow(photo[10:445,10:554])
plt.show()

plt.imshow(photo[:,:,0].T)#photo[:, :, 0] = Slicing out all rows and columns, but only keeping the 0th channel (Red)
plt.show()
# photo[:, :, 1] = Green channel only
# photo[:, :, 2] = Blue channel only
# T transpose = reverse

photo_sin = np.sin(photo)
print(photo_sin)#for finding sine values 

print(np.sum(photo))#addition
print(np.prod(photo))#product
print(np.mean(photo))#multiplication
print(np.std(photo))#stadndard deviation
print(np.var(photo))#variance
print(np.min(photo))#minimum
print(np.max(photo))#maximum
print(np.argmin(photo))#index of minimum value 
print(np.argmax(photo))#index of maximum value 

a = np.array([1,2,3,4,5])
print(a>3)
print(a<3)
a[a>3]#here we get only numbers greater than 3 in array form

b = np.array([6,7,8,9,10])

print(a+b)
print(a*b)
print(a@b)
#@if we us this @ between two arrays we get dot product of those all arrays
np.sort(a)#for sorting array

#not all but covered major part in numpy
