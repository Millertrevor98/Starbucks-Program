
name=(input("Hello welcome to Starbucks can I get your name? "))
item= str (input("What kind of coffee would you like? "))
price= float(input("what is the price? "))
quantity= int(input("what is the quantity? "))
tip= int(input("Would you like to add a tip? "))

total= price * quantity + tip
print(f"You bought {quantity} plus a tip total {item}")
print(f"And your total is ${round(total,2)}")
print("Thank you and have a good day "+name)