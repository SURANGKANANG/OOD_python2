class Stack:
    def __init__(self, list= None):
        if list== None:
            self.items= []
        else:
            self.items= list
    def push(self,i):
        self.items.append(i)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[-1]
    def isEmpty(self):
        return self.items== []
    def size(self):
        return len(self.items)
print("* Stack Calculator *")
inp = input("Enter arguments : ").split(" ") 
S = Stack()
for i in inp :
    if i == '+':
        S.push(S.pop()+S.pop())
    elif i == '-' :
        S.push(S.pop()-S.pop())
    elif i == '*':   
         S.push(S.pop()*S.pop())
    elif i == '/':   
         S.push(int(S.pop()/S.pop()))
    else:
        S.push(int(i))
if S.isEmpty():
    print(0)
else:
    print(S.pop())
    
    