# Using Ternanry Operators

for num in range(1, 101):
    output = "Fizz" if num % 3 == 0 else ""
    output += "Buzz" if num % 5 == 0 else ""
    print(num if output == "" else output)
