class linSearch:
    def __init__(self, data):
        self.data = data

    def search(self, target):
        for index, value in enumerate(self.data,):
            if value == target:
                return index
        return -1

#Array Initialization
linear = linSearch(['c', 'h', 'r', 'i', 's'])

print("========= Linear Search Operations =========")
print(linear.data)

#Find a non-existing element
print("\nSearching for 'j' in the data:")
result = linear.search('j')
if result != -1:
    print(f"Element found at index: {result}")
else:
    print("Element not found in the data.")

#Find an existing element
print("\nSearching for 'i' in the data:")
result = linear.search('i')
if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found in the data.")
