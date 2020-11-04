from metodos_para_calculo_dos_pesos.calculo_dos_pesos import CalculoDosPesos


class ObjetivoDoModelo:
    def __init__(self, resultado_obtido_pelo_modelo, entrada_esperada_1, entrada_esperada_2, padrao_desejado,
                 valor_passo, peso1, peso2, ):
        self.entrada_esperada_1 = entrada_esperada_1
        self.entrada_esperada_2 = entrada_esperada_2
        self.padrao_desejado = padrao_desejado
        self.valor_passo = valor_passo
        # self.quantidade_de_acertos_do_modelo = quantidade_de_acertos_do_modelo
        self.resultado_obtido_pelo_modelo = resultado_obtido_pelo_modelo
        self.resultado_final_do_modelo_para_funcao_e = 0
        self.pesos = CalculoDosPesos(self.valor_passo, self.entrada_esperada_1, self.entrada_esperada_2, peso1, peso2,
                                     self.padrao_desejado)

    def funcao_e(self, quantidade_de_acertos_do_modelo):
        """Função E
        e1	e2	s
        1	1	1
        1	0	0
        0	1	0
        0	0	0
        """

        if self.entrada_esperada_1 == 1 and self.entrada_esperada_2 == 1 and self.padrao_desejado == 1:
            return self.comparar_modelo_vs_funcao_e(quantidade_de_acertos_do_modelo)

        elif self.entrada_esperada_1 == 0 and self.entrada_esperada_2 == 1 and self.padrao_desejado == 0:
            return self.comparar_modelo_vs_funcao_e(quantidade_de_acertos_do_modelo)

        elif self.entrada_esperada_1 == 1 and self.entrada_esperada_2 == 0 and self.padrao_desejado == 0:
            return self.comparar_modelo_vs_funcao_e(quantidade_de_acertos_do_modelo)

        elif self.entrada_esperada_1 == 0 and self.entrada_esperada_2 == 0 and self.padrao_desejado == 0:
            return self.comparar_modelo_vs_funcao_e(quantidade_de_acertos_do_modelo)

    def comparar_modelo_vs_funcao_e(self, quantidade_de_acertos_do_modelo):
        if self.resultado_obtido_pelo_modelo == self.padrao_desejado:
            quantidade_de_acertos_do_modelo += 1
            return quantidade_de_acertos_do_modelo
        else:
            return 0

    def verificar_se_modelo_acertou(self, resultado, bias, erro):

        if len(resultado) == 3:
            print(
                f"MODELO TREINADO  COM SUCESSO PARA FUNÇÃO E \n x1-{self.entrada_esperada_1}\n x2-{self.entrada_esperada_2}\n bias-{bias}")
            return "concluído", "concluído"
        else:
            variacao_peso_1 = self.pesos.novo_peso1(erro)
            variacao_peso_2 = self.pesos.novo_peso2(erro)
            return variacao_peso_1, variacao_peso_2
