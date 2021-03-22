#Reversing the array 

def reverseArr(arr,start,end):
    while start < end:
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start +=1
        end -=1

if __name__ == '__main__':
    arr = [1,2,3,4,5,6]
    reverseArr(arr,0,len(arr)-1)
    print(arr)
