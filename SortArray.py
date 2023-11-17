def find_subarray_indices(arr):
    # Check if all elements in the array are the same
    if len(set(arr)) == 1:
        return [0, 0]
    
    # Check if the array is already sorted
    if arr == sorted(arr) or arr == sorted(arr, reverse=True):
        return [0, 0]
    
    # Find the subarray indices using stack
    stack = []
    left, right = len(arr), 0
    
    for i in range(len(arr)):
        while stack and arr[stack[-1]] > arr[i]:
            left = min(left, stack.pop())
        stack.append(i)
    
    stack = []
    
    for i in range(len(arr)-1, -1, -1):
        while stack and arr[stack[-1]] < arr[i]:
            right = max(right, stack.pop())
        stack.append(i)
    
    if right - left > 0:
        return [left, right]
    else:
        return [0, 0]
    

find_subarray_indices([1, 2, 3, 6, 4, 4])