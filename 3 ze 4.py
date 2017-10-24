# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 17:34:13 2017

Napsal: Dejvones
"""

a = input ("Obraz - Kolik řádků obrázku se má vytisknout? ")
a = int (a)
x = 0
x = a / 18

while x >= 1:
    print ("****\n***\n**\n*\n \n    *\n   ***\n  *****\n *******\n*********\n \n*\n**\n***\n****\n***\n**\n*")
    x = x - 1
y = a % 18
if y >= 1:
    print("****")
if y >= 2:
    print ("***")
if y >= 3:
    print ("**")
if y >= 4:
    print ("*")
if y >= 5:
    print (" ")
if y >= 6:
    print ("    *")
if y >= 7:
    print ("   ***")
if y >= 8:
    print ("  *****")
if y >= 9:
    print (" *******")
if y >= 10:
    print ("*********")
if y >= 11:
    print (" ")
if y >= 12:
    print ("*")
if y >= 13:
    print ("**")
if y >= 14:
    print ("***")
if y >= 15:
    print ("****")
if y >= 16:
    print ("***")
if y >= 17:
    print ("**")

b = input ("\nPro pokračování napiš ANO: ")
if b == "ANO":
    
    print ("\nŘada - Generuji kladná čísla...")
    import random
    seznam = [random.randint(0,100) for _ in range(20)]
    print ("Řada - Náš seznam:",seznam)
    a = 0
    vetsimensi = []
    delitelne = []
    for i in seznam:
        if i % 2 == 0:
            a = 1 + a
        if 19 > i > 11:
            vetsimensi.append(i)
        if i % 3 == 0:
            if i % 4 == 0:
                delitelne.append(i)
    print ("Řada - Počet sudých:",a)
    print ("Řada - Čísla, pro která platí 19 > x > 11:",vetsimensi)
    print ("Řada - Čísla dělitelná 3 a zároveň 4:",delitelne)
    
    print ("\nŘada - Generuji celá čísla...")
    seznam = [random.randint(-100,100) for _ in range(10)]
    print ("Řada - Náš seznam:",seznam)
    a = 0
    b = 0
    c = 0
    for i in seznam:
        if i > 1:
            a = 1 + a
        if i < 1:
            b = 1 +b
        c = (i*i)+c
    print ("Řada - Počet kladných čísel:",a)
    print ("Řada - Počet záporných čísel:",b)
    print ("Řada - Součet druhých mocnin:",c)
    print ("Řada - Aritmetický průměr:",sum(seznam)/len(seznam))
    d = input ("\nPro pokračování napiš ANO: ")
    if d == "ANO":
        
        a = input ("\nPosloupnost - Kolik prvků Fibonacciho posloupnosti vypsat: ")
        a = int(a)   
        b = 0
        c = 1
        while a > 0:
            print (b)
            b = c + b
            a = a - 1
            if a > 0:
                print (c)
                c = c + b
                a = a - 1
        a = input ("\nTo je prozatím vše.")