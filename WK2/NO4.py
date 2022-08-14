from array import array


def find3Numbers(A, arr_size, sum):
   if len(A) <= 2 :
      print("Array Input Length Must More Than",len(A))               
      return False 
   b = []  
   for i in range( 0, arr_size-2):
      for j in range(i + 1, arr_size-1):
         for k in range(j + 1, arr_size):
            if A[i] + A[j] + A[k] == sum and [A[i], A[j], A[k]] not in b and [A[j], A[k], A[i]] not in b and [A[k], A[i], A[j]] not in b and [A[j], A[i], A[k]] not in b and [A[i], A[k], A[j]] not in b and [A[k], A[j], A[i]] not in b: 
               b.append(sorted([A[i], A[j], A[k]]))
   print(b,end="")   
 
   
A = [int(i)for i in input("Enter Your List : ").split()]  
arr_size = len(A)
sum = 5 
find3Numbers(A,arr_size,sum)    