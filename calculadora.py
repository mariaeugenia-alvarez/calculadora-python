while True:
    try:
        a = float(input("Enter the first number: "))
        break
    except ValueError:
        print("Please enter a valid number.")

while True:
    try:
        b = float(input("Enter the second number: "))
        break
    except ValueError:
        print("Please enter a valid number.")

print("la suma es igual a,", a+b)
print("la resta es igual a,", a-b)

print("la multiplicación es igual a,", a*b)

if b!=0:
    print("la división es igual a,", a/b)

else:

    print("no se puede dividir")