_VALOR_DO_PASSO = 0.1


class CalculoDosPesos:
    def __int__(self):
        pass

    def valor_do_passo(self, valor_passo):
        return valor_passo

    def calculo_de_erro(self, padrao_a_ser_obtido, resultado_do_modelo_no_momento):
        erro = padrao_a_ser_obtido - resultado_do_modelo_no_momento
        return erro

    def calculo_variacao_peso1(self, erro, entrada_1):
        return erro * _VALOR_DO_PASSO * entrada_1

    def calculo_variacao_peso2(self, erro, entrada_2):
        return erro * _VALOR_DO_PASSO * entrada_2

    def calculo_variacao_de_bias(self, erro):
        return erro * _VALOR_DO_PASSO

    def novo_peso1(self, erro, entrada_1, peso1):
        return peso1 + self.calculo_variacao_peso1(erro, entrada_1)

    def novo_peso2(self, erro, entrada_2, peso2):
        return peso2 + self.calculo_variacao_peso2(erro, entrada_2)

    def novo_bias(self, erro, bias):
        return bias + self.calculo_variacao_de_bias(erro)
