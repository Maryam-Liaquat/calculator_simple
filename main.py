from addition import add
from subtraction import sub
from multiply import multy


if __name__ == "__main__":
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print("Addition: {} + {} = {}".format(num1,num2,add(num1,num2)))
    print("Subtraction: {} - {} = {}".format(num1,num2,sub(num1,num2)))
    print("Multiplication: {} * {} = {}".format(num1,num2,multy(num1,num2)))