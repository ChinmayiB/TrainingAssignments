#2.Bank chargings
count=0
amount=int(input("Enter the amount in your account:"))
for yet in range(1,11):
    decide=input("Tell us what you wish to do:")
    if decide=="deposit":
        money=int(input("Tell us money you wish to deposit:"))
        amount+=money
        print("Amount in your account after transaction:",amount)
    elif decide=="withdraw":
        money=int(input("Tell us money you wish to withdraw:"))
        if count<5:
            amount-=money
            print("Amount in your account after transaction:",amount)
        else:
            amount-=money+20
            print("Amount in your account after transaction:",amount)
        count+=1
