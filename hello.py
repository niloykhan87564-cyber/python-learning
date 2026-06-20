ask = int(input("Enter a number: "))

if ask > 0:
    print("Num is positive")
elif ask < 0:
    print("Num is negative")
else:
    print("Num is zero")

mull = int(input("How many times do you want to multiply your num? "))
print(f'\nMultiplication Table of {ask}:')

for i in range(1, mull + 1):
    print(f"{ask} x {i} = {ask * i}")

    print(f"{ask}X{i} = {ask*i}")