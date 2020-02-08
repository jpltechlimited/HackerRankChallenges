import numpy

arr = input().split(' ')
numpyArray = numpy.array(arr, int)
print(numpy.reshape(numpyArray,(3,3)))