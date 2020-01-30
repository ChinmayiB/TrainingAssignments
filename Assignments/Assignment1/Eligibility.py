# Eligibility for companies
# Companies are Zoho,TCS,EveryIndia,Infosys

skillset=str(input("Enter your skill set:"))
project=int(input("Enter the number of projects done by you:"))
if project>=3 and skillset=="java" or skillset=="python":
    print("You are eligible for Every India")
if project>=4 and skillset=="c" or skillset=="python":
    print("You are eligible for TCS")
if project>=2 and skillset=="c#" or skillset=="javascript" or skillset=="python":
    print("You are eligible for Infosys")
if project>=3 and skillset=="c" or skillset=="python":
    print("You are eligible for Zoho")
 
