# ESCRIBE ESTA LINEA DE CODIGO
print("Bienvenidos al entrenamiento con python, vamos a  disfrutar al maximo esta sesion")

"""
descuento en una compra:
si compras mas de $1000, optienes un descuento del 20%
pide el monto de la compra y muestra el precio final   
"""

# pedir datos por teclado al usuario int (entero) float (decimales) str (cadena de caracteres) bool (boleano 1 o 0)

compra = float(input("Digita el Valor de tu compra: "))

#si compras mas de mil $1000, obtienes un descuento del 20%
#siempre que la salida tenga mas de un camino de resoluciòn, debo implementar condicionales
#operadores combinados
#operadores de asignaciòn =, operadores aritmeticos + - * /, operadores logicos and y, or o, not
#operadores de comparaciòn ==, !=, ><, >=, <=

if compra > 1000: 
    descuento = compra * 0.2
    compra -= descuento
    #compra = compra - descuento (es igual a la linea 19 se puede cualquiera de las dos para la misma operacion)
    print(f"El descuento es de ´{descuento}, por lo tanto su valor a pagar es {compra}")