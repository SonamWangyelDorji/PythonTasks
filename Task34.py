temperature = int(float(input("Enter the temperature: ")))
if temperature >= 100:
    print("Boiling")
elif temperature>= 39 and temperature<= 99:
    print("Liquid")
elif temperature<=32:
    print("Freezing")