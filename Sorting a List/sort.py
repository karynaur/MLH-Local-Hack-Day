arr=list(map(int,input().split()))

newarray=[]

#find minimum element in sub array
def minimum(array):
  mi=array[0]
  for i in range(len(array)):
    if array[i]<mi:mi=array[i]
  return mi

#sort sub arrays and remove minimum element
for i in range(len(arr)):
  min_element=minimum(arr)
  arr.remove(min_element)
  newarray.append(min_element)
print(newarray)
