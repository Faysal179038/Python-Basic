# return statement = Functions send Python  values/objects back to the caller.
#                    These values/objects are known as the function's return value
#                    These values/objects are returned by using the return statement.


def multiply(number1, number2):
    result = number1 * number2
    return result


x = multiply(6, 8)
print(x)


def multiply(number1, number2):
    return number1 * number2


x = multiply(6, 8)
print(x)
