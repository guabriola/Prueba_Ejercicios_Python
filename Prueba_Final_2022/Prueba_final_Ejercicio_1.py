
def ejercicio_1() -> int:
    numero = str(pow(2, 1000))
    sum = 0
    for digit in numero:
        sum += int(digit)
    return sum

print(ejercicio_1())
