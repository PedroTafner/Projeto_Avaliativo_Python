import funcoes
print("\nBem vindo ao ") 

leitura=int(input("Digite o número total de leituras da pressão hidrodinâmina que serão realizadas no seu turno: "))

zVerde=0
zAmarela=0
zVermelha=0
menor = 400
leituraRealizada = 0

somaPressoes=0

for i in range(leitura):
    
    if zVermelha!= 2:
        upcAtual=float(input("Digite o valor atual da Pressão Hidrodinâmica: "))

        upcNovo=funcoes.acharNovo(upcAtual)
        
        if menor>upcNovo:
            menor = upcNovo

        somaPressoes+=upcNovo

        if upcNovo>120 and upcNovo<180:
            zVerde+=1
            zVermelha = 0
        elif upcNovo<250:
            zAmarela+=1
            zVermelha = 0
        else:
            zVermelha+=1

    else:
        print("\nO escoamento irá ser interrompido imediatamente por segurança")
        break
    leituraRealizada +=1

print("Resultados: ")
  