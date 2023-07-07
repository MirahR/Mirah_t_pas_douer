try:
    a = int(input("Entrer a : "))
    b = int(input("Entrer b : "))
    c = a / b
except ValueError as ex:
    print(ex.__doc__)

except ZeroDivisionError:
    print(ZeroDivisionError.__doc__)

except ArithmeticError:
    print(ArithmeticError.__doc__)

except NameError:
    print(NameError.__doc__)

finally:
    print("F.I.N")