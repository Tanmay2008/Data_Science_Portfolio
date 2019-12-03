import numpy
arr = [-1000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10000]
print(arr)
elements = numpy.array(arr)
print(elements)
mean = numpy.mean(elements, axis=0)
std = numpy.std(elements, axis=0)
print("Mean:", mean)
print("Std", std)
final_list = [x for x in arr if (x > mean - 2 * std)]
print(final_list)
final_list = [x for x in final_list if (x < mean + 2 * std)]
print(final_list)
