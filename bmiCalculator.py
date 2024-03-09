weight= int(input("Enter your weight in kilograms: "))
height = int(input("Enter your height in meters: "))

BMI = weight/height** 2
result_BMI = round(BMI,3)
print(f"Your weight is:{weight}kg")
print(f"Your height is:{height}m")
print(f"Your BMI is:{result_BMI}")

if BMI >0:
    if (BMI<18.5):
        print("You're underweight")
    elif (BMI<=24.9):
        print("You're normal weight")
    elif (BMI<34.9):
        print("You're obese")
    elif (BMI<39.9):
        print("You're severely obese")
    else:
        print("You're morbidly obese")
else:
    print('Invalid input \nEnter valid values')