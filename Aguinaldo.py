# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 09:44:48 2021

Nombre: Gustavo Reyes Herrera
RUT: oculto

Mis respuestas en este trabajo son propias, y están realizadas
en conformidad con la formación ética de lSa universidad.

"""

salario = input("Ingrese su sueldo: ")
categoria = input('Ingrese su categoría aqui: ')
salario = int(salario)
categoria = int(categoria)

if (categoria >= 1) and (categoria <= 15):
    if (categoria == 1):
        aguinaldo = salario * 10 // 100
    elif (categoria >= 2) and (categoria <= 3):
        aguinaldo = salario * 9 // 100
    elif (categoria >= 4) and (categoria <= 6):
        aguinaldo = salario * 7 // 100
    elif (categoria >= 7) and (categoria <= 10):
        aguinaldo = 50000
    elif (categoria >= 11) and (categoria <= 15):
        aguinaldo = 30000
    print(f'El aguinaldo es de: ${aguinaldo}')
else:
    print("Error: Categoría fuera de rango")
