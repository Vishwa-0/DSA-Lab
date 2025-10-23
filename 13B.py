def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
marks = list(map(int, input("Enter the students' marks separated by spaces: ").split()))
marks_bubble = marks.copy()
marks_selection = marks.copy()
marks_insertion = marks.copy()
bubble_sort(marks_bubble)
selection_sort(marks_selection)
insertion_sort(marks_insertion)
print("Sorted marks using Bubble Sort: ", marks_bubble)
print("Sorted marks using Selection Sort: ", marks_selection)
print("Sorted marks using Insertion Sort:", marks_insertion)
