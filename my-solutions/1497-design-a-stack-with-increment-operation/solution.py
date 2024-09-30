class CustomStack:

    def __init__(self, maxSize: int):
        # Initialize the stack with a maximum size and an array for storing increments
        self.stack = []
        self.maxSize = maxSize
        self.incrementArray = [0] * maxSize  # Store increment values for each index

    def push(self, x: int) -> None:
        # Push x to the top of the stack if it has not reached maxSize
        if len(self.stack) < self.maxSize:
            self.stack.append(x)

    def pop(self) -> int:
        # Pop and return the top of the stack, apply any stored increments to it
        if not self.stack:
            return -1
        idx = len(self.stack) - 1
        increment = self.incrementArray[idx]
        if idx > 0:
            self.incrementArray[idx - 1] += increment  # Pass the increment downwards
        self.incrementArray[idx] = 0  # Reset increment for this element
        return self.stack.pop() + increment

    def increment(self, k: int, val: int) -> None:
        # Increment the bottom k elements by val
        limit = min(k, len(self.stack))
        if limit > 0:
            self.incrementArray[limit - 1] += val

