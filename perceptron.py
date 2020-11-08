# _VALOR_DO_PASSO = 0.1
# _SEQUENCIA_ENTRADA1_ENTRADA2_SAIDA = [[1, 1, 1], [1, 0, 0], [0, 1, 0], [0, 0, 0]]
# _PESOS_DO_MODELO_TREINADO = []
#
# #------- Modelo estruturado do perceptron-------
# def valor_de_saida_do_modelo(entrada_1, variacao_peso_1, entrada_2, variacao_peso_2, bias):
#     resultado_do_modelo_no_momento = (entrada_1 * variacao_peso_1) + (entrada_2 * variacao_peso_2) + bias
#     return calculo_da_saida_do_modelo(resultado_do_modelo_no_momento)
#
#
# def calculo_da_saida_do_modelo(resultado_do_modelo_no_momento):
#     if resultado_do_modelo_no_momento > 0:
#         return 1
#     else:
#         return 0
#
#
# def funcao_e(entrada_1, entrada_2, padrao_de_saida_esperado, saida_do_modelo):
#     """Função E\n
#     entrada_1	    entrada_2	    padrao_de_saida(s)\n
#         1	           1	           1\n
#         1	           0	           0\n
#         0	           1	           0\n
#         0	           0	           0\n
#     """
#
#     if entrada_1 == 1 and entrada_2 == 1 and padrao_de_saida_esperado == 1:
#         return verifica_se_o_modelo_acertou(saida_do_modelo, padrao_de_saida_esperado)
#
#     elif (entrada_1 == 0 and entrada_2 == 1) or (entrada_1 == 1 and entrada_2 == 0) and padrao_de_saida_esperado == 0:
#         return verifica_se_o_modelo_acertou(saida_do_modelo, padrao_de_saida_esperado)
#
#     elif entrada_1 == 0 and entrada_2 == 0 and padrao_de_saida_esperado == 0:
#         return verifica_se_o_modelo_acertou(saida_do_modelo, padrao_de_saida_esperado)
#
#
# def verifica_se_o_modelo_acertou(saida_do_modelo, padrao_de_saida_esperado):
#     if saida_do_modelo == padrao_de_saida_esperado:
#         return True
#     else:
#         return False
#
#
# def valor_do_passo(valor_passo):
#     return valor_passo
#
#
# def calculo_de_erro(padrao_a_ser_obtido, resultado_do_modelo_no_momento):
#     erro = padrao_a_ser_obtido - resultado_do_modelo_no_momento
#     return erro
#
#
# def calculo_variacao_peso1(erro, entrada_1):
#     return erro * _VALOR_DO_PASSO * entrada_1
#
#
# def calculo_variacao_peso2(erro, entrada_2):
#     return erro * _VALOR_DO_PASSO * entrada_2
#
#
# def calculo_variacao_de_bias(erro):
#     return erro * _VALOR_DO_PASSO
#
#
# def novo_peso1(erro, entrada_1, peso1):
#     return peso1 + calculo_variacao_peso1(erro, entrada_1)
#
#
# def novo_peso2(erro, entrada_2, peso2):
#     return peso2 + calculo_variacao_peso2(erro, entrada_2)
#
#
# def novo_bias(erro, bias):
#     return bias + calculo_variacao_de_bias(erro)
#
#
# def treinar_modelo(nome_da_funcao):
#     bias = 1
#     peso1 = 1
#     peso2 = 1
#     for sequencia_de_teste in _SEQUENCIA_ENTRADA1_ENTRADA2_SAIDA:
#         resultado = False
#         entrada_1 = sequencia_de_teste[0]
#         entrada_2 = sequencia_de_teste[1]
#         padrao_de_saida_esperado = sequencia_de_teste[2]
#         contador_tentativas = 1
#         while resultado is False:
#             resultado_do_modelo_no_momento = valor_de_saida_do_modelo(entrada_1, peso1, entrada_2, peso2, bias)
#             resultado = funcao_e(entrada_1, entrada_2, padrao_de_saida_esperado, resultado_do_modelo_no_momento)
#             print(f"{30 * '='}\nTentativa  de número {contador_tentativas}\n{30 * '='}\n")
#             print(f"1ªEntrada->{entrada_1}\n2ªEntrada->{entrada_2}\n"
#                   f"Saída esperada->{padrao_de_saida_esperado}\nResultado do modelo->{resultado_do_modelo_no_momento}\n")
#             if resultado is True:
#                 continue
#             else:
#                 contador_tentativas += 1
#                 erro = calculo_de_erro(padrao_de_saida_esperado, resultado_do_modelo_no_momento)
#                 peso1 = novo_peso1(erro, entrada_1, peso1)
#                 peso2 = novo_peso2(erro, entrada_2, peso2)
#                 bias = novo_bias(erro, bias)
#     _PESOS_DO_MODELO_TREINADO.append({f"Pesos obtidos, para realizar função{nome_da_funcao}": [peso1, peso2, bias]})
#     return print("modelo treinado com sucesso!!!! para função e")
#
#
# treinar_modelo("FUNCAO E")
