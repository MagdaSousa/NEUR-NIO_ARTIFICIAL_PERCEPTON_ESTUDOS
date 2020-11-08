

def gravar_no_txt(resultado_do_treinamento):
    arquivo = open("perceptron.txt", "w")
    arquivo.write(str(resultado_do_treinamento[0]))