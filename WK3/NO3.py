class Stack():
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def get_size(self):
        return len(self.stack)

    def isEmpty(self):
        return len(self.stack) == 0

    def get_stack(self):
        return self.stack

    def peek(self,index: int = -1):
        if self.isEmpty(): return None
        return self.stack[index]

def extract_input(char) -> int:
    if ord(char) >= ord('A') and ord(char) <= ord('Z'):
        if s.isEmpty() or s.peek() != char or s.get_size() < 2:
            s.push(char)
        else:
            if s.get_stack()[-2] == char:
                s.pop()
                s.pop()
                return 1
            else:
                s.push(char)
    return 0

s = Stack()
combo = 0
for char in input('Enter Input : '):
    combo += extract_input(char)
print(s.get_size())
if s.get_size() == 0:
    print('Empty')
else:
    while s.get_size() > 0:
        print(s.pop(),end="")
    print('')
if combo > 1:
    print(f'Combo : {combo} ! ! !')