from tqdm import tqdm
import time
print(" ")


def Type(msg):
    D = len(msg) + 4
    print('~' * D)
    print(f'  {msg}')
    print('~' * D)


Type('Calculadora De Entalpia')
print(' ')
print('Loading... ')
with tqdm(total=100) as pbar:
    for i in range(10):
        time.sleep(0.3)
        pbar.update(10)
print("Loading completed")
print(" ")

t = input(" ")
if t == 's':
    print('\046[0;34;43m TABELA: \046[m')
    print(" ")
    print("CO2 (g) -393,4")
    print("CaO (s) -634,9 ")
    print("HI  (g) +25,9 ")
    print("NO  (g) +90,1")
else:
    print
a = int(input("senha: "))
if a == 1234:
    print(" ")
    print(" ")
    print("ΔH = ∑Hp - ∑Hr")
    print('\033[4;31;40m >H< \033[m')
    try:
        b = int(input(" "))
    except:
        print("Ponha apenas numeros! ")

    print('\033[4;31;40m >p< \033[m')
    try:
        c = int(input(" "))
    except:
        print("Ponha apenas numeros! ")

    print('\033[4;31;40m >H< \033[m')
    try:
        d = int(input(" "))
    except:
        print("Ponha apenas numeros! ")

    print('\033[4;31;40m >r< \033[m')
    try:
        e = int(input(" "))
    except:
        print("Ponha apenas numeros! ")

    r1 = b * c
    print(r1)
    r2 = d * e
    print(r2)
    r3 = r1 - r2
    print('ΔH =', r3)


else:
    print("Sla mano")

print(" ")
print("                ´¸.·*´¨) ¸.·*¨)")
print("          Feito por andreison :D")
print('(¸.·´ (¸.·" ☆")')
print(" ")