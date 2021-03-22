#Find the kth max and min element in the array.

def kthMin(arr,k):
    if k < 1 and k > len(arr):
        print("k out of range")
        return

    arr.sort()

    return arr[k-1]

def kthMax(arr,k):
    if k < 1 and k > len(arr):
        print("k out of range")
        return

    arr.sort()

    return arr[len(arr)-k]

if __name__ == "__main__":
    arr = [1,2,3,4,5]
    print(kthMin(arr,3))
    print(kthMax(arr,2))
