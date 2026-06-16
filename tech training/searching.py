#linear search
def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1
arr=[14,3,27,9,41,7,35]
target=41
idx=linear_search(arr,target)
print(f"found at index {idx}")

#binary search
def binary_search(arr,target):
    left=0
    right=len(arr)-1
    while left<right:
        mid=(left+right)//2
        if arr[mid]==target:return mid
        elif arr[mid]<target:left=mid+1
        else:right=mid-1
    return -1
arr=['a','d','e','g','i','l','q']
target='g'
idx=binary_search(arr,target)
print(f"found at index {idx}")

#jump search
import math
def jump_search(arr,target):
    n=len(arr)
    step=int(math.sqrt(n))
    prev=0
    while arr[min(step,n)-1]<target:
        prev=step
        step+=int(math.sqrt(n))
        if prev>=n: return -1
    while arr[prev]<target:
        prev+=1
        if prev==min(step,n): return -1
    if arr[prev]==target:return prev
    return -1
arr=[0,1,1,2,3,5,8,13,21,34]
target=13
idx=jump_search(arr,target)
print(f"found at index {idx}")