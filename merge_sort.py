import sys
def merge(left, right):
	i=0
	j=0
	result=[]
	while i<len(left) and j<len(right):
		if left[i]<right[j]:
			result.append(left[i])
			i+=1
		else:
			result.append(right[j])
			j+=1
	while i<len(left):
		result.append(left[i])
		i+=1
	while j<len(right):
		result.append(right[j])
		j+=1
	return result

def merge_sort(array):
	if len(array)==1:
		return array
	leftarray=merge_sort(array[:len(array)/2])
	rightarray=merge_sort(array[len(array)/2:])
	return merge(leftarray, rightarray)

array=[]
files=open(sys.argv[1])
print sys.argv[1]
for line in files:
	array.append(int(line))

result=merge_sort(array)
print result
	
	
