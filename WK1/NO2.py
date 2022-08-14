print("*** multiplication or sum ***")
X = (input("Enter num1 num2 : " ).split())
N = int(X[0])
T = int(X[1])

if(N*T)<=1000 :
    print("The result is",N*T)

else :
    print("The result is",N+T)


