print("\nBem vindo ao ") 

leitura=int(input("Digite o número total de leituras da pressão hidrodinâmina que serão realizadas no seu turno: "))

zVerde=0
zAmarela=0
zVermelha=0

for i in range(leitura):
    
    upcAtual=float(input("Digite o valor atual da Pressão Hidrodinâmica: "))
    if zVermelha!= 2:
        if upcAtual>150:
            upcNovo=upcAtual*1.08
        else:
            upcNovo=upcAtual*0.96

        if upcNovo>120 and upcNovo<180:
            zVerde+=1
            zVermelha = 0
        elif upcNovo<250:
            zAmarela+=1
            zVermelha = 0
        else:
            zVermelha+=1
    