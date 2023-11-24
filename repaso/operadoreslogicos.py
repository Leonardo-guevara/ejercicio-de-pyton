# ejercicio#1 ecuaciones 
# ( c + 5)(b^2-3ac)a^2 / 4a

def exercice_one():
    a = float(input('a : ingrese su valor '))
    b = float(input('b : ingrese su valor '))
    c = float(input('c : ingrese su valor '))
    elebado_b = b **2
    elebado_a = a **2
    value = (( c + 5)*(elebado_b - 3 *a * c)*elebado_a )/ 4*a
    return value

# ejercicio #2
# algoiritmo para ingtercambiar valores de variables

def exercice_two():
    a = (input('a : ingrese su valor '))
    b = (input('b : ingrese su valor '))
    aux = a 
    a = b
    b = aux
    value = 'a : ' + a +' b: ' + b
    return value
# ejerecio#3 
# como sacar porcentaje 
def exercice_three():
    a = float(input(' ingrese su valor '))
    p = float(input(' ingrese su porcentaje '))
    aux = a / 100
    value = aux * p 
    return value

print(exercice_three())
