def maxsubarrayofAtleastlengthK(arr,k):
    #applying kadane's algorithm 
    curr_sum = arr[0]
    max_sum = []
    max_sum.append(curr_sum)

    for i in range(1,len(arr)):
        if curr_sum < 0:
            curr_sum = 0
        if curr_sum >= 0:
            curr_sum += arr[i]

        max_sum.append(curr_sum)

    if len(arr) < k:
        return False
    
    ans = float('-inf')
    exact_sum = 0

    for i in range(k):
        exact_sum += arr[i]
    
    if exact_sum > ans:
        ans = exact_sum
    
    for i in range(k,len(arr)):
        exact_sum = exact_sum+arr[i]-arr[i-k]
        if curr_sum > ans:
            ans = curr_sum
        atleast_sum = exact_sum + max_sum[i-k]
        if atleast_sum > ans:
            ans = atleast_sum

    return ans

if __name__ == '__main__':
    arr = [2,3,1,-7,6,-5,-4,4,3,3,2,-9,-5,6,1,2,1,1]
    print(maxsubarrayofAtleastlengthK(arr,4))
