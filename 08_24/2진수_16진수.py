def Bbit_print(i):
    output = ""
    for j in range(7, -1, -1):
        if i & (1 << j) == 1:
            output += "1"
        else:
            output += "0"
    return output
a = 0x10
x = 0x01020304
print(x)
output = ''
for j in range(31,-1,-1):
    # output += "1" if x & (1 << j) else "0"
    if x & (1 << j) == 1:
        output += "1"
    else:
        output += "0"
print(x)

print(Bbit_print(5))

