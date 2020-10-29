class CalculoDosPesos():
    def __init__(self, valor_passo, entrada_1, entrada_2, padrao_a_ser_obtido):
        self.entrada_1 = entrada_1
        self.entrada_2 = entrada_2
        self.peso_1 = 0
        self.peso_2 = 0
        self.padrao_a_ser_obtido = padrao_a_ser_obtido
        # self.resultado_do_modelo_no_momento = resultado_do_modelo_no_momento
        self.bias = 0
        # self.erro = 0
        self.valor_passo = valor_passo

    def valor_do_passo(self):
        return self.valor_passo

    def calculo_de_erro(self, resultado_do_modelo_no_momento):
        erro = self.padrao_a_ser_obtido - resultado_do_modelo_no_momento
        return erro

    def calculo_variacao_peso1(self, erro):
        return erro * self.valor_do_passo() * self.entrada_1

    def calculo_variacao_peso2(self, erro):
        return erro * self.valor_do_passo() * self.entrada_2

    def calculo_variacao_de_bias(self, erro):
        return erro * self.valor_do_passo()

    def novo_peso1(self, erro):
        return self.peso_1 + self.calculo_variacao_peso1(erro)

    def novo_peso2(self, erro):
        return self.peso_1 + self.calculo_variacao_peso2(erro)

    def novo_bias(self, erro):
        return self.bias + self.calculo_variacao_de_bias(erro)
