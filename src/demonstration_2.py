"""
Your goal is to define a `Queue` class that uses two stacks. Your `Queue` class
should have an `enqueue()` method and a `dequeue()` method that ensures a
"first in first out" (FIFO) order.

As you write your methods, you should optimize for time on the `enqueue()` and
`dequeue()` method calls.

The Stack class that you will use has been provided to you.
"""
class Stack:
    def __init__(self):
        self.data = []
        
    def push(self, item):
        self.data.append(item)

    def pop(self):
        if len(self.data) > 0:
            return self.data.pop()
        return "The stack is empty"

class QueueTwoStacks:
    def __init__(self):
        self.stack = Stack()
        self.shuffleStack = Stack()

    def enqueue(self, item):
        # If the shuffle stack is not empty, we need to pop and push those elements back on to the original stack
        while len(self.shuffleStack.data) > 0:
            currItem = self.shuffleStack.pop()
            self.stack.push(currItem)

        self.stack.push(item)


    def dequeue(self):
        # If the stack is empty, do nothing and return None
        if len(self.stack.data) == 0:
            return None

        # pop and push items to the shuffle stack to reverse the order of the original stack (giving us a FIFO order)
        while len(self.stack.data) > 0:
            currItem = self.stack.pop()
            self.shuffleStack.push(currItem)

        return self.shuffleStack.pop()


myQueue = QueueTwoStacks()

myQueue.enqueue(1)
myQueue.enqueue(2)
myQueue.enqueue(3)
myQueue.enqueue(4)

print(myQueue.dequeue())
