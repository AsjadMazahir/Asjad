class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Capacity cannot be negative")
        self._capacity = capacity
        self._size = 0
    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if n + self.size > self.capacity:
            raise ValueError("Exceeded capacity")
        self._size = self._size + n

    def withdraw(self, n):
        if n > self.size:
            raise ValueError("Cannot withdraw more cookies than capacity")
        self._size = self._size - n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

def main():
    jar = Jar(7)
    jar.deposit(3)
    print(jar)

if __name__ == "__main__":
    main()