import numpy

def arrays(arr):
    result = numpy.array(arr, float)
    return result[::-1]

arr = input().strip().split(' ')
result = numpy.array(arr, float)
print(arrays(result))