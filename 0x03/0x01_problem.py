def func2(arr, N):
    arr_100 = [0] * 100
    for i in range(N):
        if arr_100[100 - arr[i]] == 1:
            return 1
        else:
            arr_100[arr[i]] = 1
    
    return 0

test_cases_nums = [[[1, 52, 48], 3], [[50, 42], 2], [[4, 13, 63, 87], 4]]
    
for nums, N in test_cases_nums:
    print(func2(nums, N))
        