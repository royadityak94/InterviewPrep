

def find_element(arr, ele, idx):
    if arr:
        mid = len(arr)//2
        if arr[mid] == ele:
            return mid+idx+1
        elif arr[mid] < ele:
            return find_element(arr[mid+1:], ele, mid+1)
        else:
            return find_element(arr[:mid], ele, idx)
    return None

def main():
    print (find_element([1, 2, 5, 7], 8, 0))

main()
