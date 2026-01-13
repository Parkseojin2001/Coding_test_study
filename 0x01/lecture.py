import math
import time

def func1(N):
    cnt = 0
    for i in range(1, N + 1):
        if i % 3 == 0 or i % 5 == 0:
            cnt += i

    return cnt

def func1_prime(N):
    cnt_3 = (N // 3) * (N // 3 + 1) // 2
    cnt_5 = (N // 5) * (N // 5 + 1) // 2
    cnt_15 = (N // 15) * (N // 15 + 1) // 2
    return 3 * cnt_3 + 5 * cnt_5 - 15 * cnt_15

def func2(nums, N):
    left, right = 0, N - 1
    nums.sort()
    while left < right:
        if nums[left] + nums[right] == 100:
            return 1
        elif nums[left] + nums[right] < 100:
            left += 1
        else:
            right -= 1
    return 0

def func3(N):
    for i in range(N):
        if i * i > N:
            break
        elif i * i == N:
            return 1
    return 0

def func4(N):
    cnt = 1
    while 2 * cnt <= N:
        cnt *= 2
    return cnt

def main():
    print("\n문제 1")
    print("Big-O O(N) vs O(1)")
    print("-------------------------")
    
    test_cases = [16, 34567, 27639]
    start = time.time()
    
    for case in test_cases:
        print(func1(case))
    end = time.time()
    print(f"func1 - O(N) time: {end - start:.6f} seconds")
    
    start = time.time()
    for case in test_cases:
        print(func1_prime(case))
    end = time.time()
    print(f"func1_prime - O(1) time: {end - start:.6f} seconds")
    
    print("\n문제 2")
    
    test_cases_nums = [[[1, 52, 48], 3], [[50, 42], 2], [[4, 13, 63, 87], 4]]
    
    for nums, N in test_cases_nums:
        print(func2(nums, N))
        
    print("\n문제 3")
    test_cases_N = [9, 693953651, 756580036]
    for N in test_cases_N:
        print(func3(N))
    
    print("\n문제 4")
    test_cases_N = [5, 97615282, 1024]
    for N in test_cases_N:
        print(func4(N))

if __name__ == "__main__":
    main()
