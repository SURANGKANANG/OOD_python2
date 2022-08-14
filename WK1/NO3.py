from tabnanny import check

print("*** Election ***")
votes_numbers = []
def most_frequent(number_votes): #หาค่าซ้ำกันมากที่สุด 
    counter = 0
    num = number_votes[0]
     
    for i in number_votes:  
        curr_frequency = number_votes.count(i)
        if(curr_frequency> counter and i <=20 and i > 0):
            counter = curr_frequency
            num = i
 
    return num

number_List = int(input("Enter a number of voter(s) : "))
number_votes = [int(i)for i in input().split()]
checkbuddee = 0
for i in range(1,21) :
    if i in number_votes :
        checkbuddee =1
        
if checkbuddee == 1 :
    print(most_frequent(number_votes))
    
else :
    print("*** No Candidate Wins ***")