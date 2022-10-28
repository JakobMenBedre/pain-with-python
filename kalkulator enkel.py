from ctypes.wintypes import INT


tall1 = int(input())

tall2 = int(input())

addisjon = tall1 + tall2

subtraksjon = tall1 - tall2

multiplisering = tall1 * tall2

deling = tall1 / tall2

regneopperasjon = input("+ for plussing. - for minus. * for ganging. / for deling.\n")
if regneopperasjon == '+':
    print(addisjon)
elif regneopperasjon == '-':
    print(subtraksjon)
elif regneopperasjon == '*':
    print(multiplisering)
elif regneopperasjon == '/':
    print(deling)




