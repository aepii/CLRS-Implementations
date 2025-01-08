class DynamicStack:
    def __init__(self, capacity):
        self._capacity = capacity 
        self._stack = [None] * capacity 
        self._top = -1

    @property
    def stack_empty(self):
        return self._top == -1
    
    @property
    def stack_full(self):
        return self._top == self._capacity - 1
    
    @property
    def capacity(self):
        return self._capacity
    
    @property
    def size(self):
        return self._top + 1

    def _resize(self, multiplier):
        new_capacity = max(4, int(self._capacity * multiplier))
        new_stack = [None] * new_capacity

        for i in range(self.size):
            new_stack[i] = self._stack[i]

        self._capacity = new_capacity
        self._stack = new_stack

    def push(self, x):
        if self.stack_full:
            self._resize(2)

        self._top += 1
        self._stack[self._top] = x

    def pop(self):
        if self.stack_empty:
           raise ValueError("Stack is empty.")

        self._top -= 1

        if self.size <= self.capacity / 4:
            self._resize(1/2)

        return self._stack[self._top + 1]
    
    def peek(self):
        if self.stack_empty:
            raise ValueError("Stack is empty.")
        
        return self._stack[self._top]

    def __repr__(self):
        return f"{self._stack[:self._top + 1]}"

# BadabaNonDuck