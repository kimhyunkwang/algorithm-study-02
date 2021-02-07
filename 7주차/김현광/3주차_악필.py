a, b = input().split()

def seven_to_nine(string):
    string = string.replace('7', '9')
    return int(string)

def nine_to_seven(string):
    string = string.replace('9', '7')
    return int(string)

maximum = seven_to_nine(a) + seven_to_nine(b)
minimum = nine_to_seven(a) + nine_to_seven(b)

print(maximum, minimum)