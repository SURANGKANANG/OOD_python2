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


       
p = Stack()
j = Stack()
s = input("Enter Input : ").split(",")

for i in s:
    if i[0] == 'A' :
        p.push(int(i[2:]))
        print("Add = "+i[2:])
    elif i[0] == 'P' :
        if p.isEmpty():
            print("-1")
        else:
            print("Pop = "+str(p.pop()))
    elif i[0] == 'D' :
        if p.isEmpty():
            print("-1")
        else:
            while not p.isEmpty():  #รันไปเรื่อยๆจนกว่ามันจะว่าง
                a=p.pop()
                if a != int(i[2:]) :
                    j.push(a) 
                else:
                    print("Delete = "+str(a))
            while not j.isEmpty():p.push(j.pop())
    elif i[0] == 'L' :
        if p.isEmpty():
            print("-1") 
        else:
            while not p.isEmpty():  #รันไปเรื่อยๆจนกว่ามันจะว่าง
                a=p.pop()
                if a >= int(i[3:]) :
                    j.push(a) 
                else:
                    print("Delete = "+str(a),"Because "+str(a),"is less than "+str(int(i[3:])))
            while not j.isEmpty():p.push(j.pop())
    else:
        if p.isEmpty():
            print("-1") 
        else:
            while not p.isEmpty():  #รันไปเรื่อยๆจนกว่ามันจะว่าง
                a=p.pop()
                if a <= int(i[3:]) :
                    j.push(a) 
                else:
                    print("Delete = "+str(a),"Because "+str(a),"is more than "+str(int(i[3:])))
            while not j.isEmpty():p.push(j.pop())
w = []
while not p.isEmpty():
    w.append(p.pop())
print("Value in Stack = "+str(w[::-1]))