x = int(input("Insert first number: "))
y = int(input("Insert second number: "))
operation = input("Insert operation (+ - * /): ")

if operation == "+":
    print (x + y)
elif operation == "-":
    print (x - y)
elif operation =="*":
    print (x * y)
elif operation == "/":
    print (x / y)
else:
    print ("Sorry, I don't get it.")