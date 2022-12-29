def xiaoxin(x_1, y_1, x_2, y_2):

    if x_2 == x_1 and y_2 == y_1:
        return "Entrées invalides! "
    elif x_2 == x_1:
        return f"x = {x_1}"
    elif y_2 == y_1:
        return f"f(x) = {y_1}"
    else:
        a = (y_2 - y_1) / (x_2 - x_1)
         
        b = y_1 - a * x_1
        if b == int(b):
            b = int(b)
        if b == 0:
            b = ""
        elif b > 0:
            b = f" + {b}"
        else:
            b = f" - {-b}"
    return (f"f(x) = {a}x{b}")


print(xiaoxin(2, 7, 5, 19))
print(xiaoxin(2, 7, 2, 7))
print(xiaoxin(2, 7, 2, 10))
print(xiaoxin(2, 7, 10, 7))
