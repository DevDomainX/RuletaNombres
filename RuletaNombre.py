#!/usr/bin/env python3
# -*- encoding: utf - 8 -*-

from random import choice
from colorama import init, Fore, Style
init()

names = []
con = 0
print(Fore.YELLOW+Style.BRIGHT+"""Selector de nombre al azar Script

        Created by: Hans Saldias\n\n""")
      
c = input("cuantos nombres vas a ingresar:  ")
while not c.isdigit():
    c = input("cuantos nombres vas a ingresar:  ")

c = int(c)
    
while con < c:
    con += 1
    name = input("Ingrese nombre: ")
    names.append(name)
res = choice(names)
print(res)

while True:
    p = input("Desea volver a elegir otro nombre con los mismos datos (si/no): ")
    
    if p == "si":
        pass
    res = choice(names)
    print(f"\nEl nombre seleccionado es: {res}\n")
    if p == "no":
        print("Gracias por usar mi script")
        break
    