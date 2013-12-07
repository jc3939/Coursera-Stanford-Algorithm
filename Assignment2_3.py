import sys
global count
count=0
def swap(series,i,j):
    tmp=series[i]
    series[i]=series[j]
    series[j]=tmp
def sortpivot(series):
    first=series[0]
    last=series[-1]
    middle=series[(len(series)/2)-1+(len(series)%2)]
    L=[first,middle,last]
    L.sort()
    if L[1]==first:
        return 0
    elif L[1]==middle:
        return (len(series)/2)-1+(len(series)%2)
    else:
        return -1
    
def quicksort(series):
    global count
    if len(series)<=1:
        return series
    else:
        pi=sortpivot(series)
        pivot=series[pi]
        swap(series,0,pi)
        pi=0
        i=pi
        j=1
        while j<len(series):
            count +=1
            if series[j]<pivot:
                i=i+1
                swap(series,i,j)
            j=j+1
        swap(series,i,pi)
        pi=i
        #print series
        #print pi
        left=quicksort(series[:pi])
        right=quicksort(series[pi+1:])
        L=[series[pi]]
        if len(left)==0:
            result=L+right
        elif len(right)==0:
            result=left+L
        else:
            result=left+L+right
        result=map(int,result)
        return result


datafile=open(sys.argv[1])
data=[]
for number in datafile:
    data.append(number)
data=map(int,data)
result=quicksort(data)
print result,count
