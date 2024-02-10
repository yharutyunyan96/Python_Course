#ex1_adress
#name = input("Enter your name: ")
#surname = input ("Enter your surname: ")
#Email = input ("Enter your email adress: ")
#Country = input ("Enter your country: ")
#City = input("Enter your city: ")
#Street_home_number = input("Enter your street and home number: ")
#print ("Name:",name,"\n","Surname:",surname,"\n","Email:",Email,"\n","Adress:",Country, City, Street_home_number,)

#ex2_greeting
#Name = input("Enter your name:")
#print ("Hello", Name, end=":")

#ex3_room_Area
#length = float( input("Enter the length of your room:"))
#width = float (input ("Enter the width of your room:"))
#area = length * width
#print("The area of your room is:", area)

#ex4_area_of_fieald
#import math 
#length = float(input("Enter the length of the field in feet:"))
#width = float(input("Enter the width of the field in feet:"))
#area = round((length * width) / 43.560, 3)
#print(area)
#print ( 5e-3)

#ex5_bottle_deposit
import math
#bottle_weight = float(input("Enter your bottle's quantity less than 1litre:"))
#bottle_weight_2 = float(input("Enter your bottle's quantity more than 1 litre:"))
#quantity = round( bottle_weight * 0.10 + bottle_weight_2 * 0.25, 2)
#print ("Your deposit equals:", quantity ,"$")

#ex6_Tax_tips
#meal = float (input("Enter your meal price:"))
#tax = round(meal * 0.2, 2)
#tip = round(meal * 0.18, 2)
#total = round(meal + tax + tip, 2)
#print("Your meal price is:",meal,"\n",'Your tip is:',tip,"\n","The amount of the tax is:",tax,"\n","Total amount is:",total)

#ex7_Sum of the N
#num = math.factorial(int(input("Enter your number:")))
#total = round((num*(num + 1))/2, 2)
#print (total)

#ex8_widgets and gizmos
#widgets = float (input("Enter the number of widgets you require:"))
#gizmos = float (input("Enter the number of gizmos you require:"))
#wid_weight = widgets * 75
#giz_weight = gizmos * 112
#print ("The total weight of widgets you requires is",wid_weight,"\n","The total weight of gizmos you required is:",giz_weight,)

#ex9_interest
#bank_account = float(input("Enter the amount in your account per year:"))
#Year_1 = round(bank_account * 0.04, 2)
#Year_2 = round(Year_1 + (Year_1 * 0.04), 2)
#Year_3 = round(Year_2+ (Year_2 * 0.04), 2)
#print ("The total interest in your account in 3 years is:",Year_1 + Year_2 + Year_3)

#ex10_arithmatic
#a = float(input("Enter first number:"))
#b = float(input("Enter second number:"))
#sum = a+b
#sub = a-b
#product = a*b
#div = a/b
#reminder = a%b
#log = math.log10 (a)
#sqr = a**b
#print (sum,sub,product,div,reminder,log,sqr, sep = "\n")

#ex11_Fuel efficiency
#USA = float(input("Enter the fuel efficiency:"))
#sum = round(USA * 235.2145)
#print ("Your fuel efficiency in Canada's system is:", sum,"L/100")

#ex12_distance
#from math import radians
#t1 = radians(float(input("Enter the latitude of your first point:")))
#t2 = radians(float(input("Enter the latitude of your second point:")))
#g1 = radians(float(input("Enter the longitude of your first point:")))
#g2 = radians(float(input("Enter the longitude of your second point:")))
#distance = round(6372.03 * math.acos(math.sin(t1) * math.sin(t2) +  math.cos(t1) * math.cos(t2) * math.cos(g1 + g2)), 2)
#print ("The distance between two points is:", distance)
                   
#ex13_change
payment = float(input("Enter your money in cents:"))
toonie = payment // 200
loonie = float(payment - toonie*200) // 100
quarters = float(payment %100)// 25
nickles = float(payment %100 - quarters*25) //10
pennies = float(payment %100 - quarters*25 -nickles*10)//5
cents = float(payment %100 -  quarters*25 - nickles*10- pennies*5)
print("Your change is:","\n","Toonies:",toonie,"\n","Loonies:",loonie,"\n","Quarters:",quarters,"\n","Nickles:",nickles,"\n","Pennies:",pennies,"Cents",cents,"\n" )

#should'n we use if and else in this example? so for ex. money = 200,then from then start it will just give 2 200s,