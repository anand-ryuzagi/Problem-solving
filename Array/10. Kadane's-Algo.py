def kadaneAlgo(arr):
    current_sum = 0
    maximum_sum = 0
    start =0
    end = 0
    pointer = 0
    for i in range(len(arr)):
        current_sum  = current_sum + arr[i]
        
        
        if current_sum < 0:
            current_sum = 0
            pointer = i+1
        
        if maximum_sum < current_sum:
            start = pointer
            end= i
            maximum_sum = current_sum

    return start, end, maximum_sum

if __name__ == '__main__':
    arr = [4,-3,-2,2,3,1,-2,-3,6,-6,-4,2,1]
    start,end,sum = kadaneAlgo(arr)
    print(start,end,sum)
