import logging

logging.basicConfig(filename="mylog.log",level=logging.debug)

try:
    f = open("myfile","w")
    a,b = [int(x) for x in input("Enter two numbers:").split()]
    c = a/b
    print(c)
    f.write("Writing %d into file")
except ZeroDivisionError:
    print("Division by zero is not allowed")
    print("Please enter a non zero number")
    logging.error("Division by zero")
else:
    print("You have entered a non-zero number")
finally:
    f.close()
    print("File closed")
print("Code after the exception")