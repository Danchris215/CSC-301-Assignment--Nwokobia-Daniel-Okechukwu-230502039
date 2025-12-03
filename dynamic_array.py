class DynamicArray:
    def __init__(self):
        self.capacity = 2 
        self.size = 0
        self.data = [None]*self.capacity

    def append(self, value):
        if self.size == self.capacity:
            self.resize()
        self.data[self.size] = value
        self.size += 1
    def resize(self):
        self.capacity = self.capacity * 2
        new_data = [None] * self.capacity 
        for i in range(self.size):
            new_data[i] = self.data[i]
        self.data = new_data 

dynamic_array = DynamicArray()
dynamic_array.append(10)
dynamic_array.append(20)
dynamic_array.append(30)
dynamic_array.append(40)
dynamic_array.append(50)

print(dynamic_array.data)