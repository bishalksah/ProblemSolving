print("Enter the first array elements separated by space:")
arr1 = list(map(int, input().split()))

print("Enter the second array elements separated by space:")
arr2 = list(map(int, input().split()))

def merge_arrays(arr1 ,arr2):
    mergedArray = arr1 + arr2
    sort_array(mergedArray)
    return mergedArray

# arr=[6,7,8,9,4,5,6,89,9]
def sort_array(mergedArray):
    print(f"{"i":<2} {"j":<2} {"m[i]":<5} {"m[j]":<5}  {"m"}")
    for i in range(len(mergedArray)):
        for j in range(i + 1, len(mergedArray)):
            if mergedArray[i] > mergedArray[j]:
                mergedArray[i], mergedArray[j] = mergedArray[j], mergedArray[i]
                
            print(f"{i:<2} {j:<2} {mergedArray[i]:<5} {mergedArray[j]:<5}  {mergedArray}")
    return mergedArray

result = merge_arrays(arr1, arr2)
print("Merged and sorted array:", result)
    
  
    
    
    