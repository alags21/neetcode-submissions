class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.backing_array = []

    def get(self, i: int) -> int:
        return self.backing_array[i]

    def set(self, i: int, n: int) -> None:
        self.backing_array[i] = n

    def pushback(self, n: int) -> None:
        if self.getSize() == self.getCapacity():
            self.resize()
        self.backing_array.append(n)

    def popback(self) -> int:
        return self.backing_array.pop(-1)

    def resize(self) -> None:
        self.capacity = self.capacity * 2
        return

    def getSize(self) -> int:
        return len(self.backing_array)
    
    def getCapacity(self) -> int:
        return self.capacity
