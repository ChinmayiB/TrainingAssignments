#bus chart
chart=""
for row in range(1,8):
    for seat in range(1,5):
        amount=int(input("Tell us the amount you have:"))
        if amount>=300:
            print("Your seat number is:",row,seat)
            chart+="$"
        else:
            print("You don't have sufficient amount")
            chart+="#"
    chart+="\n"
print(chart)
            
