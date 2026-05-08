num_1 = float(input('First number: '))
num_2 = float(input('Second number: '))
op = input('Operation: ')

if op == "+":
    result = num_1 + num_2
elif op == "-":
    result = num_1 - num_2
elif op == "*":
    result = num_1 * num_2
elif op == "/":
    result = num_1 / num_2
elif op == "%":
    result = num_1 % num_2
elif op == "**":
    result = num_1 ** num_2
else:
    print('that aint an operator')
    result = "nope"
print(num_1, op, num_2, "=", result)