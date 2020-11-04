from objetivos_do_modelo.funcoes_para_testar_modelo import ObjetivoDoModelo
from metodos_para_calculo_dos_pesos.calculo_dos_pesos import CalculoDosPesos


class TreinoModelo:
    def __init__(self):
        self.sequencia_x1_x2_padrao = [[1, 1, 1], [1, 0, 0], [0, 1, 0], [0, 0, 0]]
        self.valor_do_passo = 0.1
        self.variacao_peso_1 = 0
        self.variacao_peso_2 = 0
        self.valor_calculado_de_saida =0
        self.teste=[]

    def valor_de_saida_do_modelo(self, entrada_1, variacao_peso_1, entrada_2, variacao_peso_2, bias):
        resultado_do_modelo_no_momento = (entrada_1 * variacao_peso_1) + (entrada_2 * variacao_peso_2) + bias
        return resultado_do_modelo_no_momento

    def calculo_da_saida_do_modelo(self, resultado_do_modelo_no_momento):

        if resultado_do_modelo_no_momento > 0:
            return 0
        else:
            return 1

    def sequencia_de_entradas_para_funcao_e(self):
        # resultado_do_modelo_no_momento = 0
        while self.variacao_peso_1 != "concluído":
            for x in self.sequencia_x1_x2_padrao:
                self.calculo_dos_pesos = CalculoDosPesos(self.valor_do_passo,
                                                         x[0],
                                                         x[1],
                                                         self.variacao_peso_1,
                                                         self.variacao_peso_2,
                                                         x[2])
                erro = self.calculo_dos_pesos.calculo_de_erro(self.valor_calculado_de_saida)
                bias = self.calculo_dos_pesos.novo_bias(erro)
                saida_do_modelo_no_momento = self.valor_de_saida_do_modelo(x[0],
                                                                           self.variacao_peso_1,
                                                                           x[1],
                                                                           self.variacao_peso_2,
                                                                           bias)
                self.valor_calculado_de_saida = self.calculo_da_saida_do_modelo(saida_do_modelo_no_momento)

                self.variacao_peso_1 = self.calculo_dos_pesos.calculo_variacao_peso1(erro)
                self.variacao_peso_2 = self.calculo_dos_pesos.calculo_variacao_peso2(erro)

                carregar_modelo = ObjetivoDoModelo(saida_do_modelo_no_momento,
                                                   x[0],
                                                   x[1],
                                                   x[2],
                                                   self.valor_do_passo,
                                                   self.variacao_peso_1,
                                                   self.variacao_peso_2)
                quantidade_de_acertos_do_modelo = carregar_modelo.funcao_e(len(self.teste))

                self.teste.append(quantidade_de_acertos_do_modelo)
                self.variacao_peso_1, self.variacao_peso_2 = carregar_modelo.verificar_se_modelo_acertou(
                    self.teste,
                    bias,
                    erro)
                if self.variacao_peso_1 == "concluído":
                    break
