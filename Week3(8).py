number = int(input("Enter a number: "))

if number < 0:
    number = abs(number)
    for i in range(12, -1, -1):
        result = number * i
        print(f"{number} times {i} is {result}")

    else:
         for i in range(13):
             result = number * i
             print(f"{number} times {i} is {result}")
             break
