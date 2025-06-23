W = float(input("Enter weight KG:"))
H = float(input("/enter height Meters:"))

bmi = W / (H ** 2)


print("YOUR BMI:" , bmi)

if bmi < 18.5:
    print("UNDERWEIGHT")
elif 18.5 <= bmi < 24.9:
    print("Your weight is average")
elif 25 <= bmi <29.9:
    print("Overweight")
else:
    print("OBESE")

