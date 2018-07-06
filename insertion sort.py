#program to peform insertion sort

def insertion_sort(array1):
 length = len(array1)
 for x in range(1, length):
     while x > 0 and array1[x - 1] > array1[x]:
         array1_temp = array1[x]
         array1[x] = array1[x - 1]
         array1[x - 1] = array1_temp
         print(array1[x], array1[x - 1])
         x -= 1

 return array1

length = input("Enter the length of the array ?")
x = 0
arry1 = []
while x < length:
    value = int(input(" Enter the element"))
    arry1.append(value)
    x +=1
print(type(arry1),arry1)
insertion_sort(arry1)
print(arry1)
