def convert_celsius_to_fahrenheit(temp_celsius):
    temp_fahrenheit = temp_celsius * 1.8 + 32
    return temp_fahrenheit


def convert_fahrenheit_to_celsius(temp_f):
    temp_c = (temp_f - 32) / 1.8
    return temp_c


temp_in_f = convert_celsius_to_fahrenheit(28)

print(temp_in_f)

temp_in_c = convert_fahrenheit_to_celsius(85)

print(temp_in_c)
