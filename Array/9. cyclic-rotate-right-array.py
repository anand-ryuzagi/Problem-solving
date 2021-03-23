def rotateRight(arr,d):
    start = 0
    end = len(arr)-1
    reverse(arr,start,end-d)
    reverse(arr,end-d+1,end)
    reverse(arr,start,end)

def reverse(arr,start,end):
    while start<end:
        temp = arr[start]
        arr[start] =arr[end]
        arr[end] = temp
        start +=1
        end-=1

arr = [1,2,3,4,5,6]
rotateRight(arr,1)
print(arr)
