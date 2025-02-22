def soma(a,b,c):
    return a+b+c

print(soma(5,3,4))
print(soma(5,2,2))

def multiplicacao(d,e,f):
    return d*e*f

print(multiplicacao (1,8,3))
print(multiplicacao (9,4,4))

def bemvindo():
    print("wellcome")

def menor(a,b):
    if a<=b:
        return a
    else:
        return b 
print(menor (25, 15))


def velocidademedia(tempo, distancia):
    return distancia/tempo

distancia=float(input("digite a distancia"))
tempo=float(input("digite o tempo em horas"))

print(velocidademedia(tempo,distancia))