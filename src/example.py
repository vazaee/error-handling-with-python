def divide(n1, n2):
    if not (isinstance(n1, int) and isinstance(n2, int)):
        raise ValueError("divide() must receive only integer arguments")
    try:
        aux = n1 / n2
    except:
        print(f"Could not divide {n1} by {n2}")
        raise
    return aux

def test_division(n1):
    result = divide(10,n1)
    print(f"10 divided by {n1} is {result}")

#try:
#    test_division(0)
#except ZeroDivisionError as E:
#    print("Attribute error")
#except Exception as E:
#    print("Generic treatment")

try:
    print("Flow is here")
    raise ValueError
except Exception:
    print("Now it is here")

print("Then in continues...")


try:
    test_division(0)
except AttributeError:
    print("attribute error")
print("program finished")