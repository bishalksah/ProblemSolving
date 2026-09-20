print("Enter the first array elements separated by space:")
arr1 = list(map(int, input().split()))

print("Enter the second array elements separated by space:")
arr2 = list(map(int, input().split()))

def merge_sort(arr1 ,arr2):
    merged = arr1 + arr2
    merged.sort()
    return merged

print("Merged and sorted array:", merge_sort(arr1, arr2))
