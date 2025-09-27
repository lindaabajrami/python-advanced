from gettext import textdomain

try:
    result = 10/0
except ZeroDivisionError:
    print("error, tried to divide by zero.")

text = "this is not a number"

try:
    text_to_int = int(text)
except Exception as e:
    print("an error occured while parsing the date: " , e)

try:
    result = 10/2
except ZeroDivisionError:
    print("error, tried tp divide by zero.")
else:
    print("division successful. result: ", result)