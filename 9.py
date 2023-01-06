class Stack:

    def __init__(self):
        self.Elements = []

    def push(self, value):
        self.Elements.append(value)

    def pop(self):
        return self.Elements.pop()

    def empty(self):
        return self.Elements == []

    def show(self):
        for value in reversed(self.Elements):
            print(value)


def BottomInsert(self, value):
    if self.empty():
        self.push(value)

    else:
        popped = self.pop()
        BottomInsert(self, value)
        self.push(popped) 

def Reverse(self):
    if self.empty():
        pass
    else:
        popped = self.pop()
        Reverse(self)
        BottomInsert(self, popped)


stk = Stack()
stk.push(100)
stk.push(200)
stk.push(300)
stk.push(40)
stk.push(50)

print("Original Stack")
stk.show()

print("\nStack after Reversing")
Reverse(stk)
stk.show()