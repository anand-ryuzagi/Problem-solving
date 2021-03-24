def maxsubarrayoflengthK(arr,k):
    if len(arr) < k:
        return False
    
    ans = 0
    curr_sum = 0

    for i in range(k):
        curr_sum += arr[i]
    
    if curr_sum > ans:
        ans = curr_sum
    
    for i in range(k,len(arr)):
        curr_sum = curr_sum+arr[i]-arr[i-k]
        if curr_sum > ans:
            ans = curr_sum


    
    return ans

if __name__ == '__main__':
    arr = [1,2,3,4,5]
    print(maxsubarrayoflengthK(arr,4))
