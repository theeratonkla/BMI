import math

weight = float(input("Please Enter Your Weight (kilogram) : "))
height = float(input("Please Enter Your Height (centimeter) : "))
height = height / 100
bmi = weight / (height ** 2)
print(bmi)
if bmi < 18.5:
    print("You're in the underweight range.")
    print("Being underweight could be a sign you're not eating enough or you may be ill.")
elif bmi < 24.9:
    print("You're in the healthy weight range.")
    print("Keep up the good work!")
elif bmi < 29.9:
    print("You're in the overweight range.")
    print("The best way to lose weight if you're overweight is through a combination of diet and exercise.")
else:
    print("You're in the obese range.")
    print("The best way to lose weight if you're obese is through a combination of diet and exercise")
x = int(input('''
Please select Do you want to continue or end:
1 for continue
0 for end
 '''))
while x == 1:
    weight = float(input("Please Enter Your Weight (kilogram) : "))
    height = float(input("Please Enter Your Height (centimeter) : "))
    height = height / 100
    bmi = weight / (height ** 2)
    print(bmi)
    if bmi < 18.5:
        print("You're in the underweight range.")
        print("Being underweight could be a sign you're not eating enough or you may be ill.")
    elif bmi < 24.9:
        print("You're in the healthy weight range.")
        print("Keep up the good work!")
    elif bmi < 29.9:
        print("You're in the overweight range.")
        print("The best way to lose weight if you're overweight is through a combination of diet and exercise.")
    else:
        print("You're in the obese range.")
        print("The best way to lose weight if you're obese is through a combination of diet and exercise")
    x = int(input('''
Please select Do you want to continue or end:
1 for continue
0 for end
 '''))
