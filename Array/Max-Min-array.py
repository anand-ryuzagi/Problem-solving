#Time complexity : O(n)
#Find the minimum and maximum element of an array

def maxmin(arr):
    max = 0
    min = 0
    if len(arr) == 1:
        max = arr[0]
        min = arr[0]
    
    if arr[0]<arr[1]:
        min = arr[0]
        max = arr[1]
    else:
        min = arr[1]
        max = arr[0]

    for i in range(2,len(arr)):
        if arr[i] < min:
            min = arr[i]
        elif arr[i] > max:
            max = arr[i]
    

    return min, max

if __name__ =='__main__':
    arr = [1,6,3,4,5,1]
    minimum,maximum = maxmin(arr)
    print("Minimum in array is: ",minimum)
    print("Maximum in array is: ",maximum)
