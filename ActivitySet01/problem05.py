# Functions


def computepay(h, r):
    pass  # ...


hrs = float(input("Enter hours? "))
rte = float(input("Enter rate per hour? "))

'''p = computepay(hrs, rte)
print("Pay", p)
def Sum(a,b):
    c=a+b
    return c
def mul(a,b):
    f=a*b
    return f
a = int(input())
b = int(input())

Add =Sum(a,b)
# print(Add)
mul =mul(a,b)
# print(mul)
print(Add+mul)
''''
def computepay(h, r):
    if hrs <= 40:
        p = hrs*rate
    elif hrs > 40:
        p = 40*rate+(hrs-40)*rate*1.5
    
    return p

hrs = float(input("Enter Hours:"))
rate =float(input("Enter rate"))

p = computepay(10, 20)
print("Pay", p)