Count_bid = [int(i)for i in input("Enter All Bid : ").split()]
Count_bid.sort()

if len(Count_bid)<=1 :
    print ("not enough bidder")
    
elif Count_bid[-1] == Count_bid[-2] :
    print ("error : have more than one highest bid")
    
else :
        print("winner bid is "+str(Count_bid[-1])+" need to pay "+str(Count_bid[-2]))
