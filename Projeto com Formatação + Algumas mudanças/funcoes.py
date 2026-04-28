def acharNovo(upcAtual):
    if upcAtual > 150:
        upcNovo = upcAtual*1.08

    else:
        upcNovo = upcAtual*0.96

    return upcNovo


def menor(menor,upcNovo):
    if menor > upcNovo:
        menor = upcNovo
    
    return menor


def resultados(mediaPressoes, menor, zVerde,porcentagemDeLeitura ):
    print("\n-------------------------------------------------------------------------------------------------------")
    print('\n\tRESULTADO DAS LEITURAS DA REFINARIA:')
    print(f'\n\tA media das pressões foi de {mediaPressoes:.2f}')
    print(f'\tO menor UPC registrado foi {menor:.2f}')
    print(f'\tO total de Zonas Verdes registradas foi de {zVerde}')

    if porcentagemDeLeitura != 100:
        print(f'\tA porcentagem de leituras realizadas é de {porcentagemDeLeitura:.2f}%')
        
    print("\n-------------------------------------------------------------------------------------------------------")


def classificacao(upcNovo,zAmarela,zVerde,zVermelha):    
    if upcNovo > 120 and upcNovo < 180:
        zVerde += 1
        zVermelha = 0   
    
    elif upcNovo > 180 and upcNovo < 250:
        zAmarela += 1
        zVermelha = 0
    
    else:
        zVermelha += 1
    
    return zAmarela,zVerde,zVermelha


def media(somaPressoes, leituraRealizada):
   resultado = somaPressoes / leituraRealizada
   return resultado

def porcentagem(leituraRealizada, leitura):
   resultado = (leituraRealizada/leitura) * 100
   return resultado