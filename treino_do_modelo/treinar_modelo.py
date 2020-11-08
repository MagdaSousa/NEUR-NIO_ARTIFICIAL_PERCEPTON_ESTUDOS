from funcoes_para_ensinar_o_modelo.funcoes_para_testar_modelo import EnsinarModelo
from calculo_dos_pesos.calculo_dos_pesos import CalculoDosPesos

_PESOS_DO_MODELO_TREINADO = []


class TreinoModelo:
    def __init__(self, nome_da_funcao, _SEQUENCIA_ENTRADA1_ENTRADA2_SAIDA, funcao_para_treino):
        self.nome_da_funcao = nome_da_funcao
        self.sequencial_para_ensinar_o_modelo = _SEQUENCIA_ENTRADA1_ENTRADA2_SAIDA
        self.ensinar_modelo = EnsinarModelo()
        self.calculo_dos_pesos = CalculoDosPesos()
        self.funcao_para_treino = funcao_para_treino

    def valor_de_saida_do_modelo(self, entrada_1, variacao_peso_1, entrada_2, variacao_peso_2, bias):
        """Calcula o valor de saída do modelo e chama o método calculo_da_saida_do_modelo,
        para transformar o resultado em um valor binário para comparação"""

        resultado_do_modelo_no_momento = (entrada_1 * variacao_peso_1) + (entrada_2 * variacao_peso_2) + bias
        return self.calculo_da_saida_do_modelo(resultado_do_modelo_no_momento)

    def calculo_da_saida_do_modelo(self, resultado_do_modelo_no_momento):
        if resultado_do_modelo_no_momento > 0:
            return 1
        else:
            return 0

    def treinar_modelo(self,funcao_para_treino):
        """ treina o perceptrom de acordo com a função escolhida"""
        bias = 1
        peso1 = 1
        peso2 = 1
        for sequencia_de_teste in self.sequencial_para_ensinar_o_modelo:
            resultado = False
            entrada_1 = sequencia_de_teste[0]
            entrada_2 = sequencia_de_teste[1]
            padrao_de_saida_esperado = sequencia_de_teste[2]
            contador_tentativas = 1
            while resultado is False:
                resultado_do_modelo_no_momento = self.valor_de_saida_do_modelo(entrada_1, peso1, entrada_2, peso2, bias)
                resultado = eval(f' self.ensinar_modelo.{funcao_para_treino}{(entrada_1,entrada_2,padrao_de_saida_esperado,resultado_do_modelo_no_momento)}')
                print(f"{30 * '='}\nTentativa  de número {contador_tentativas}\n{30 * '='}\n")

                print(f"1ªEntrada->{entrada_1}\n2ªEntrada->{entrada_2}\n"
                      f"Saída esperada->{padrao_de_saida_esperado}\n"
                      f"Resultado do modelo->{resultado_do_modelo_no_momento}\n")
                if resultado is True:
                    continue
                else:
                    contador_tentativas += 1
                    erro = self.calculo_dos_pesos.calculo_de_erro(padrao_de_saida_esperado,
                                                                  resultado_do_modelo_no_momento)
                    peso1 = self.calculo_dos_pesos.novo_peso1(erro, entrada_1, peso1)
                    peso2 = self.calculo_dos_pesos.novo_peso2(erro, entrada_2, peso2)
                    bias = self.calculo_dos_pesos.novo_bias(erro, bias)
        _PESOS_DO_MODELO_TREINADO.append({f"Pesos obtidos, para realizar função{self.nome_da_funcao}": [peso1, peso2, bias]})

        return print("modelo treinado com sucesso!!!! para função e")
