year = int(input("Enter a year to check if it's a leap year or not? "))

# divisable by 4 = leap year
# exception is if it's divisable by 100 - not a leap year
# but exception if if it's divisable by 400 - leap year

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap Year")
        else:
            print("Not a Leap year")
    else:
        print("Leap year")

else:
    print("Not a Leap Year")