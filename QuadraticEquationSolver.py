import re
import math

quad_input = str(input(print("Input your equation: ")))
quad_input = quad_input.strip()
replaced_input = ""
numbers =[]
roots = []
if quad_input[0] != 'x':
    replaced_input = quad_input.replace('x^2','').replace('x', '')
else:
    replaced_input = quad_input.replace('x^2', '1').replace('x', '')


numbers = [int(d) for d in re.findall(r'-?\d+', replaced_input)]

a = int(numbers[0])
b = int(numbers[1])
c = int(numbers[2])

discriminant = (b*b) - (4*a*c)

if discriminant >=0:
    root1 = ((-b) + math.sqrt(discriminant))/(2*a)
    root2 = ((-b) - math.sqrt(discriminant))/(2*a)
    roots.extend([root1, root2])
    print("Base equation: " + quad_input)
    print("Solutions: " + str(roots))
else:
    print("No roots")
