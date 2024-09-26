# Python3 implementation of QuickSort 
  
  
# Function to find the partition position
def partition(arr, l, h):
  low, high = l, h
  if l != h and l < h:
    # Choose the leftmost element as pivot
    pivot = arr[l][1]
    low = low+1
    # Traverse through all elements
    # compare each element with pivot
    while low <= high:
      if arr[high][1] > pivot and arr[low][1] < pivot:
        arr[high], arr[low] = arr[low], arr[high]
      if not arr[low][1] < pivot:
        low += 1
      if not arr[high][1] > pivot:
        high -= 1
  arr[l], arr[high] = arr[high], arr[l]
  # Return the position from where partition is done
  return high
  
# Function to perform quicksort
def quick_sort(array, low, high):
  if low < high:
  
      # Find pivot element such that
      # element smaller than pivot are on the left
      # element greater than pivot are on the right
      pi = partition(array, low, high)
  
      # Recursive call on the left of pivot
      quick_sort(array, low, pi - 1)
  
      # Recursive call on the right of pivot
      quick_sort(array, pi + 1, high)
  
  
          
