#IT company hiring
count=1
while count<=20:
    name=input("Tell us your name:")
    tech=str(input("Tell us the technology u r familiar with:"))
    if tech=="java" or tech=="python" or tech=="script":
        if count==1 or count==5 or count==3 or count==2 or count==6 or count==10 or count==14:
            print("The position ",count," is already booked")
            count+=1
        else:
            print("You are hired to the position ",count)
            count+=1
    else:
        print("Better luck next time")

    
    
