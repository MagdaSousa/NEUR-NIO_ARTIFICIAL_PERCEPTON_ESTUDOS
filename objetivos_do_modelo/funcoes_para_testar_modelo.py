class ObjetivoDoModelo:
    def __init__(self,entrada_esperada_1,entrada_esperada_2,resultado_obtido_pelo_modelo):
        self.entrada_esperada_1 = entrada_esperada_1
        self.entrada_esperada_2 = entrada_esperada_2
        self.padrao_desejado = 0
        self.resultado_obtido_pelo_modelo = resultado_obtido_pelo_modelo

    def funcao_e(self):
        """Função E
        e1	e2	s
        1	1	1
        1	0	0
        0	1	0
        0	0	0
        """
        if self.entrada_esperada_1 == 1 and self.entrada_esperada_2 == 1:
            self.padrao_desejado = 1
            self.verificar_resultado()
        elif (self.entrada_esperada_1 == 1 and self.entrada_esperada_2 == 0) or \
                (self.entrada_esperada_1 == 0 and self.entrada_esperada_2 == 1) or \
                (self.entrada_esperada_1 == 0 and self.entrada_esperada_2 == 1):
            self.padrao_desejado = 0
            self.verificar_resultado()

    def verificar_resultado(self):
        if self.resultado_obtido_pelo_modelo == self.padrao_desejado:
            return True
        else:
            return False
