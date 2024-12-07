# #es un ciclo que suele contener otros ciclos,es decir, hay uno externo y hay uno interno 
# #(esto no implica entonces que solamente se puedan anidar 2). Se usan para procesar datos
# #de diferente niveles o dimensiones

# #for papa in range(3):
# #    for zanahoria in range(3):
# #       print(f"i={papa}, j={zanahoria}")

# #se aplica para procesar matrices, generar patrones visuales, resolver problemas jerarquicos
#         #como tableros o graficos

# #El concepto clave es que por cada iteracion del ciclo externo, el ciclo interno ejecuta completamente


# #Procesamiento de matrices con ciclos anidados 
# #Matriz em IT: es una lista[], donde cada elemnto es una lista o una sublista, estas van a representar una fila

# matriz = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# for fila in matriz:
#     for elemento in fila:
#         print(elemento, end=" ")  #El end es para que quede en el mismo renglon y no hacia abajo
#     print()   #este print es para realizar un salto hacia abajo en la impresion
# # 1 2 3     
# # 4 5 6
# # 7 8 9
    
# suma = 0
# for fila in matriz:
#     for elemento in fila:
#         suma += elemento
# print(f"suma total: {suma}")

# contador_pares = 0

# for fila in matriz:
#     for elemento in fila:
#         if elemento % 2 == 0:
#             contador_pares += 1
# print(f"hay {contador_pares} numeros pares en la matriz")
