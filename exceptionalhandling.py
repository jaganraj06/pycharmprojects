#exceptionalhandling
try:
    num = int(input(" enter any numerator: "))
    den = int(input(" enter any denomenator : "))
    result = num/den
    print(result)

except ZeroDivisionError:
    print("some error occurred . don't use zero")
except ValueError:
    print("some error occurrred .don't use any values other then integers")

print(" THANKYOU ")
