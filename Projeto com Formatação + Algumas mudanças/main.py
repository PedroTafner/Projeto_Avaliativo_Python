import funcoes as f
print("\nBem vindo ao programa da Refinaria Delta-9") 

leitura = int(input("Digite o número total de leituras da pressão hidrodinâmina que serão realizadas no seu turno: "))

zVerde = 0
zAmarela = 0
zVermelha = 0
menor = 400
leituraRealizada = 0
somaPressoes = 0

while leitura <= 0:
    print("Número de leitura inválida, tente novamente.")
    leitura = int(input("\nDigite o número total de leituras da pressão hidrodinâmina que serão realizadas no seu turno: "))

print("\n-------------------------------------------------------------------------------------------------------")
for i in range(leitura):
    if zVermelha != 2: 
        upcAtual = float(input(f"\nLeitura N°{i+1}\nDigite o valor da Pressão Hidrodinâmica: "))
        
        upcNovo = f.acharNovo(upcAtual)
        menor = f.menor(menor, upcNovo)

        if upcNovo > 120:
            somaPressoes += upcNovo
            zAmarela, zVerde, zVermelha = f.classificacao(upcNovo,zAmarela,zVerde,zVermelha)
        
        else:
            print("\n-------------------------------------------------------------------------------------------------------")
            print("\n\tERRO DETECTADO:\n\tO fluido foi cristalizado devido a baixa pressão constrita e entupiu o duto, interrompendo o escoamento.")
            
            leituraRealizada += 1
            break
        
    else:
        print("\n-------------------------------------------------------------------------------------------------------")
        print("\nERRO DETECTADO:\n\tDevido à alta pressão constrita, o escoamento será interrompido imediatamente por segurança.")
        break
             
    leituraRealizada += 1


porcentagemDeLeitura = f.porcentagem(leituraRealizada, leitura)
mediaPressoes = f.media(somaPressoes,leituraRealizada)
f.resultados(mediaPressoes, menor, zVerde, porcentagemDeLeitura)

input("\nAperte ENTER para finalizar...")
  