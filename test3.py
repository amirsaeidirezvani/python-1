from cmath import tan
import math

num1 = int(input("num 1: "))
num2 = int(input("num 2: "))

op = input("op: ")

if op == '+':
    result = num1 + num2
    print(result)

elif op == '-':
    result = num1 - num2
    print("result")

elif op == '*':
    result = num1 * num2
    print("result")

elif op == '**':
    result = num1 ** num2
    print("result")


elif op == '/':
    if num2 == 0:
        print('nemishe!!!!')
        
    else:
        result = num1 / num2
    print('result')
##################################################


username = "asghar"
password = "1234"

input_username = input("please enter username:")
input_password = input("please enter password:")


if username == input_username and password == input_password:
    print("hello , welcome")

else:
    print("hhhhhoyyy eshtebah zady")

##################################################

r = input("lotfan shoa ro benevis yare:")
r = int(r)
mohit = (r + r) * math.pi
print(mohit)
print("................................" ".........")
name = 'maryam'
family = 'boone'
age = '22'

print("hello maryam and Amir", name,family,age, "old")
print("................................" ".........")
##################################################

a = 52
b = 56 
c = 85

result = a + a + b + c

print("result is: ", result)
print("................................" ".........")
##################################################
c = 10
f = c * 9 / 5 + 32
print(f)
print("................................" ".........")
d = input()
d = int(d)

f = d * 9 / 5 + 32
print(f)
print("................................" ".........")
