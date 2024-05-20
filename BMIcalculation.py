#bmi


height = float(input("enter your height in m:"))
weight = float(input("enter your wight in kg:"))

def BMI (height,weight):
    bmi = weight/height**2
    if(bmi<16):
        return 'severely underweight',bmi
    elif(bmi>=16 and bmi<18.5):
        return 'under weight',bmi
    elif(bmi>=18.5 and bmi<25):
        return 'helthy',bmi
    elif(bmi>=25 and bmi<30):
        return 'overweight',bmi
    elif(bmi>=30):
        return 'obese',bmi
quote,bmi = BMI(height,weight)

print(quote)
print(bmi)



