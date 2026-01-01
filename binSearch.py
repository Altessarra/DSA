class binSearch:
    def __init__(self, data):
        self.data = data
        self.data.sort()
        
    def search(self, target):
        low = 0
        high = len(self.data) - 1

        while low <= high:
            mid = (low + high) // 2
            if self.data[mid] == target:
                return mid  
            elif self.data[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1
  
binary = binSearch()
  
print("========= Binary Search Operations =========")
data = [34, 7, 23, 32, 5, 62]
binary = binSearch(data)
print("Array: ", data)
print("Array (sorted):", binary.data)

#First Search: 23
target = 23
result = binary.search(target)
if result != -1:
    print(f"\nSearching for {target}: \nFound at index {result}")
else:
    print(f"\nSearching for {target}: \nNot Found")

#Second search: 100
target2 = 100
result2 = binary.search(target2)
if result2 != -1:
    print(f"\nSearching for {target2}: \nFound at index {result2}")
else:
    print(f"\nSearching for {target2}: \nElement not found")