def odd_even(type, data, mode):
    if type == "S" : 
        if mode == "Odd" :
            for i in range(0, len(data),2): #ในโปรเเกรมมันเริ่มจาก 0 
                print(data[i],end="")
        else :
             for i in range(1, len(data),2):
                print(data[i],end="")
    else :
        L = data.split() #ให้คำมันเเยกออกจากกันเป็นตัวๆ
        if mode == "Odd" :
            L = [L[i] for i in range(0, len(L),2)]
        else :
              L = [L[i] for i in range(1, len(L),2)]
                
        print(L)
    
print("*** Odd Even ***")    
t,d,m = input("Enter Input : ").split(",")
odd_even(t, d, m)