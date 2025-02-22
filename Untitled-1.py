DDD={61:"BRASILIA", 11:"SAO PAULO", 71:"SALVADOR"}

iDDD = int(input ("digite o numero do DDD:"))

if iDDD in DDD:
    print (DDD[iDDD])
else:
    print("Nao tem no dicionario")