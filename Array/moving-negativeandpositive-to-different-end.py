# Move all negative numbers to beginning and positive to end with constant extra space



def partition(arr):
    i = -1
    pivot = 0

    for j in range(0,len(arr)):
        if(arr[j]<pivot):
            i += 1
            arr[i],arr[j] = arr[j],arr[i]

if __name__ =='__main__':
    arr=[-9,-10,6,-4,1,-12]
    partition(arr)
    print(arr)
