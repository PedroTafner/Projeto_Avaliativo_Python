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
    
    if zVermelha!= 2 and upcNovo>120:

        upcAtual=float(input("Digite o valor atual da Pressão Hidrodinâmica: "))

        upcNovo=funcoes.acharNovo(upcAtual)
        
        menor = funcoes.menor(menor, upcNovo)

        somaPressoes+=upcNovo
    
        zAmarela, zVerde, zVermelha = funcoes.classificacao(upcNovo,zAmarela,zVerde,zVermelha)

    else:
        print("\nO escoamento irá ser interrompido imediatamente por segurança")
        break
    leituraRealizada +=1

funcoes.resultados(menor, zAmarela, zVerde)
  