#!/usr/bin/python3
from file import add, sub, mul, div

a = 10
b = 5

add_result = add(a, b)
sub_result = sub(a, b)
mul_result = mul(a, b)
div_result = div(a, b)

print(str(a) + " + " + str(b) + " = " + str(add_result))
print(str(a) + " - " + str(b) + " = " + str(sub_result))
print(str(a) + " * " + str(b) + " = " + str(mul_result))
print(str(a) + " / " + str(b) + " = " + str(div_result))
