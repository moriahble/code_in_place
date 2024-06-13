def convert_celsius_to_fahrenheit(temp_celsius):
    temp_fahrenheit = temp_celsius * 1.8 + 32
    return temp_fahrenheit


temp_in_f = convert_celsius_to_fahrenheit(28)

print(temp_in_f)