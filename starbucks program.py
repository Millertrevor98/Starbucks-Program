#Create inputs and add strings or integers
name=(input("Hello welcome to Starbucks can I get your name? "))
item= str (input("What kind of coffee would you like? "))
price= float(input("what is the price? "))
quantity= int(input("what is the quantity? "))
tip= int(input("Would you like to add a tip? "))
#Add up all of the inputs you make in the console and if you don't want to add a tip put 0 
total= price * quantity + tip
#This outputs all of the information you inputed in the console
print(f"You bought {quantity} plus a tip total {item}")
print(f"And your total is ${round(total,2)}")
print("Thank you and have a good day "+name)
