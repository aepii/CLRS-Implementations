class StaticStack:
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

    def push(self, x):
        if self.stack_full:
            raise ValueError("Stack full.")
        self._top += 1
        self._stack[self._top] = x

    def pop(self):
        if self.stack_empty:
           raise ValueError("Stack empty.")
        self._top -= 1
        return self._stack[self._top + 1]
    
    def __repr__(self):
        return f"{self._stack[:self._top + 1]}"