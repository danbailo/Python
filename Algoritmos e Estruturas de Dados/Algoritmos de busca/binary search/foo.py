# Python Program for recursive binary search. 
  
# Returns index of x in arr if present, else -1 
def binarySearch (arr, l, r, x): 
  
    # Check base case 
    if r >= l: 
  
        mid = int(l + (r - l)/2)
  
        # If element is present at the middle itself 
        if arr[mid] == x: 
            return mid 
          
        # If element is smaller than mid, then it  
        # can only be present in left subarray 
        elif arr[mid] > x: 
            return binarySearch(arr, l, mid-1, x) 
  
        # Else the element can only be present  
        # in right subarray 
        else: 
            return binarySearch(arr, mid + 1, r, x) 
  
    else: 
        # Element is not present in the array 
        return -1

def BBRecurs(A, p, r, x):
    if p == r-1:
	    return r
    else: 
        q = int((p+r)/2)
        if A[q] < x:
            return BBRecurs(A, q, r, x)
        else:
            return BBRecurs(A, p, q, x)

# Test array 
# arr = [ 2, 3, 4, 10, 40 ] 
arr = [3, 41, 52, 26, 38, 57, 9, 49]
x = 3
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print("Element is present at index % d" % result) 
else: 
    print("Element is not present in array")

array = [1,2,3,4,5,6,7,8,9,10]

print(BBRecurs(array,0,len(array)+1,9))