# Queue using two stacks
class QueueUsingTwoStacks:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def enqueue(self, x):
        self.in_stack.append(x)

    def dequeue(self):
        self._shift_stacks()
        if self.out_stack:
            self.out_stack.pop()

    def peek(self):
        self._shift_stacks()
        if self.out_stack:
            print(self.out_stack[-1])

    def _shift_stacks(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

# Read and process input
q = int(input())
queue = QueueUsingTwoStacks()

for _ in range(q):
    query = input().strip().split()
    if query[0] == '1':
        queue.enqueue(int(query[1]))
    elif query[0] == '2':
        queue.dequeue()
    elif query[0] == '3':
        queue.peek()
