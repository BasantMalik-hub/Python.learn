print("welcome to tip calculator") 
total_bill = float(input("what was the total bill? $") )
per_tip = int(input("how much tip you would like to give? 10 , 12 , or 15? "))
total_people = int(input("how many people to split the bill?"))
tip = ((((per_tip/100)*total_bill)+total_bill)/total_people)
print(f"each person should pay: ${round(tip,2)}")

