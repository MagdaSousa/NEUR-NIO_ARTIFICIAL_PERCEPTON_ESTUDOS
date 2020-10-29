from objetivos_do_modelo.funcoes_para_testar_modelo import ObjetivoDoModelo
from metodos_para_calculo_dos_pesos.calculo_dos_pesos import CalculoDosPesos


class TreinoModelo:
    def __init__(self):
        self.chamar_funcao_para_treino = ''
        self.calculo_dos_pesos = ''
        self.sequencia = [[1, 1, 1], [1, 0, 0], [0, 1, 0], [0, 0, 0]]
        self.valor_do_passo = 0.1

    def calculo_da_saida_do_modelo(self, entrada_1, variacao_peso_1, entrada_2, variacao_peso_2, bias):
        resultado_do_modelo_no_momento = (entrada_1 * variacao_peso_1) + (entrada_2 * variacao_peso_2) + bias
        if resultado_do_modelo_no_momento > 0:
            return 0
        else:
            return 1

    def sequencia_de_entradas_para_funcao_e(self):
        resultado_do_modelo_no_momento = 0
        variacao_peso_1: int = 0
        variacao_peso_2: int = 0
        for x in self.sequencia:
            self.calculo_dos_pesos = CalculoDosPesos(self.valor_do_passo, x[0], x[1], x[2])
            erro = self.calculo_dos_pesos.calculo_de_erro(resultado_do_modelo_no_momento)
            variacao_peso_1 = self.calculo_dos_pesos.calculo_variacao_peso1(erro)
            variacao_peso_2 = self.calculo_dos_pesos.calculo_variacao_peso2(erro)
            bias = self.calculo_dos_pesos.novo_bias(erro)
            resultado_do_modelo_no_momento = self.calculo_da_saida_do_modelo(x[0], variacao_peso_1, x[1],
                                                                             variacao_peso_2, bias)

            variacao_peso_1 = self.calculo_dos_pesos.novo_peso1(erro)
            variacao_peso_2 = self.calculo_dos_pesos.novo_peso2(erro)

    def mostrar_resultado_do_modelo(self):
        pass
