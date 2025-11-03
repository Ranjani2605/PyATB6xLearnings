age = int(input("Enter the age :").strip())

if age <= 0 or age > 130:
    print("Enter a valid age")

else:
    if age > 22:
        print("They can go to goa")
    else:
        print("They can't go to goa")


# find the number is even or off

num = int(input("Enter the number: ").strip())

if num >=0 :
    if num % 2 == 0:
        print("even number")
    else:
        print("odd number")
else:
    print("Negative Number")

# you can write short one-liner conditions using ternary operators:

if num >= 0:
    print('even number' if num % 2 == 0 else 'odd number')
else:
    print('Negative Number')
