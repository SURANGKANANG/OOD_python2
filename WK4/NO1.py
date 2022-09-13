class Queue:
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
    def front(self):
        return self.items[0] if self.size()>0 else -1
    
    def enqueue(self,tmp):
        self.items.append(tmp)
    
    def dequeue(self):
        return self.items.pop(0) if self.size()>0 else -1
    
a=input("Enter Input : ").split(",")
Q = Queue()
p = Queue()
R = Queue()
for i in a:
    if i[0] == 'E' :
        Q.enqueue(int(i[2:]))
        while not Q.isEmpty():
            if Q.size() == 1 :
               print(Q.front()) 
            else :
               print(Q.front(),end=", ")
            p.enqueue(Q.dequeue())
        while not p.isEmpty():
            Q.enqueue(p.dequeue())
    else :
        if Q.isEmpty():
            print("Empty")
        else:
            print(Q.front(),end=" <- ")
            R.enqueue(Q.dequeue())
            if Q.isEmpty() :
                print("Empty")
            else:
                while not Q.isEmpty():
                    if Q.size() == 1 :
                        print(Q.front()) 
                    else :
                        print(Q.front(),end=", ")
                    p.enqueue(Q.dequeue())
                while not p.isEmpty():
                    Q.enqueue(p.dequeue())
if R.isEmpty() :
    print("Empty : ",end="")
else:
    while not R.isEmpty() :
        if R.size() == 1 :
            print(R.dequeue(),end=" : ") 
        else :
            print(R.dequeue(),end=", ")
if Q.isEmpty() :
    print("Empty")
else:
    while not Q.isEmpty() :
        if Q.size() == 1 :
            print(Q.dequeue()) 
        else :
            print(Q.dequeue(),end=", ")
           
        