import sys
import random
def select_pivot(array):
	index=random.randint(0,len(array)-1)
	print index, len(array)
	return array[index]

def quick_sort(array):
	left=[]
	right=[]
	if len(array)<=1:
		return array
	pivot=select_pivot(array)
	array.remove(pivot)
	for i in array:
		if i<pivot:
			left.append(i)
		if i>pivot:
			right.append(i)
	
	return quick_sort(left)+[pivot]+quick_sort(right)
	
files=open(sys.argv[1])
array=[]
for line in files:
	array.append(int(line))

print quick_sort(array)
