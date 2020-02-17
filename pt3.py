string = "my scooters are made of steel"
result = ' '
for i in string:
    if i == 'm':
        i = '$'
    elif i == 's':
        i = '@'
    result +=i
print(result)