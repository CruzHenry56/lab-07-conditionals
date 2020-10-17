import sys

print ("BMI CAL VOL 1")
weight = input("What is your weight (in pounds) ? ")

height = input("What is your height (in inches) ? ")

bmi = (703 * float(weight)) / float(height) * float(height)

print("Your Body mass index (BMI) is " + str(bmi) +"%")
