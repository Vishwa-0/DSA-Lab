def linear_search(arr, target):
    for i in arr:
        if i == target:
            return True
    return False

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False
registered_students = list(map(int, input("Enter all registered roll numbers separated by spaces: ").split()))
roll_number = int(input("Enter the roll number to search: "))
found_linear = linear_search(registered_students, roll_number)
print(f"Linear Search: Roll number {'found' if found_linear else 'not found'}.")
registered_students.sort()
found_binary = binary_search(registered_students, roll_number)
print(f"Binary Search: Roll number {'found' if found_binary else 'not found'}.")
