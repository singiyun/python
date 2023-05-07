def say_hello(user_name="anonymous"):
    print("Hello", user_name)

say_hello("singiyun")
say_hello()

def plus(a=0, b=0):
    print(a+b)

def minus(a=0, b=0):
    print(a-b)

def multiply(a=0, b=0):
    print(a*b)

def divide(a=0, b=1):
    print(a/b)

def power(a=0, b=1):
    print(a**b)

plus(9,5)
minus(11,2)
multiply(4,2)
divide(6,2)
power(3,2)

plus()
minus()
multiply()
divide()
power()