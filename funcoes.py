def mediaTotal(x,y):
    mediaPressoes = x / y
    return mediaPressoes

def acharNovo(upcAtual):
    if upcAtual>150:
            upcNovo=upcAtual*1.08
    else:
        upcNovo=upcAtual*0.96
    return upcNovo