def divide(n1, n2):
    # print(n2.result)
    return n1/n2

def test_division(n1):
    try:
        result = divide(10,n1)
        print(f"10 divided by {n1} is {result}")
    except ZeroDivisionError:
        print ("Division by zero error")

try:
    test_division(0)
except AttributeError:
    print("attribute error")

print("program finished")