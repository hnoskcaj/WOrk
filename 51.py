integer= 12345
output = ""
a = len(str(integer))
for x in range(a):
  output = output + str(integer%10) + " "
  integer = integer // 10

print(output)