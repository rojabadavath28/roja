def gcd(a,b):
    """
    compute the greatest common divisor(gcd)of two numbers using the eucledean algorithm.
    :param a:first number(integer).
    :param b:second number(integer).
    :return:gcd of a and b.
    """
    while b!=0:
      a,b=b,a%b
  #update ato b and b to the remainder of a divided by b
    return a
num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
result=gcd(num1, num2)
print(f" the gcd of {num1} and {num2} is :{result}")

