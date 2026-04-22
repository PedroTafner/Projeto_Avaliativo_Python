def mediaTotal(x,y):
    mediaPressoes = x / y
    return mediaPressoes

def acharNovo(upcAtual):
    if upcAtual>150:
            upcNovo=upcAtual*1.08
    else:
        upcNovo=upcAtual*0.96
    return upcNovo

def menor(menor,upcNovo):
    if menor>upcNovo:
        menor = upcNovo
    return menor


def resultados(menor, zAmarela, zVerde):
    print('RESULTADOS')
    print('------------------------')
    print(f'O menor UPC registrado foi {menor:.2f}')
    print(f'O total de Zonas Verdes registradas foi de {zVerde}')
    print(f'O total de Zonas Amarelas registradas foi de {zAmarela}')


def classificacao(upcNovo,zAmarela,zVerde,zVermelha):
    if upcNovo<120:
        print("O fluido foi cristalizado e entupiu")
    elif upcNovo>120 and upcNovo<180:
        zVerde+=1
        zVermelha = 0
            
    elif upcNovo>180 and upcNovo<250:
        zAmarela+=1
        zVermelha = 0
    else:
        zVermelha+=1
    return zAmarela,zVerde,zVermelha