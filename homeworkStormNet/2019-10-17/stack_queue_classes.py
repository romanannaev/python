# # stack
# class Stack(list):
#     pass

# stack = Stack(i for i in range(1, 11))
# while stack:
#     print(stack.pop())
# print('next queue')
# #queue
# class Queue(list):
#     pass
# queue = Queue(i for i in range(1,11))
# while queue:
#     print(queue.pop(0))


class Stack:
    def __init__(self):
        self.items = [1, 2,]

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)
# lst = Stack()
# lst.push(3)
# print(lst.pop())
# print(lst.items)
print(Stack.__dict__)
