class EnsinarModelo:
    def __init__(self):
        pass

    def funcoes_para_treino(self):
        """ dicionário com o nome da função para treino,
         e a sunção que contem a 'tabela verdade', ou valor em binário que representará  o valor a ser obtido"""

        funcoes = {1: ['funcao_e', self.sequencial_binario_para_funcao_e()]}
        return funcoes

    def escolher_funcoes(self, numero_da_funcao):
        """ Escolhe a função para treinar o neurônio a partir do número passado pelo usuário"""
        nome_da_funcoes = self.funcoes_para_treino()
        for key in nome_da_funcoes:
            if key == numero_da_funcao:
                return nome_da_funcoes[key]

    def sequencial_binario_para_funcao_e(self):
        """ este método representa as entradas e saída esperada para a função E, em binário.
        No caso a 1ª e a 2ª caso da lista são as entradas e a 3ª é o resultado esperado"""
        _SEQUENCIA_ENTRADA1_ENTRADA2_SAIDA = [[1, 1, 1], [1, 0, 0], [0, 1, 0], [0, 0, 0]]
        return _SEQUENCIA_ENTRADA1_ENTRADA2_SAIDA

    def funcao_e(self, entrada_1, entrada_2, padrao_de_saida_esperado, saida_do_modelo):
        """Função que será utilizada para ensinar o modelo, no caso vamos ensinar a função E\n

        Função E:\n
        entrada_1      entrada_2	    padrao_de_saida(s)\n
            1	           1	           1\n
            1	           0	           0\n
            0	           1	           0\n
            0	           0	           0\n
        """

        if entrada_1 == 1 and entrada_2 == 1 and padrao_de_saida_esperado == 1:
            return self.verifica_se_o_modelo_acertou(saida_do_modelo, padrao_de_saida_esperado)

        elif (entrada_1 == 0 and entrada_2 == 1) or (
                entrada_1 == 1 and entrada_2 == 0) and padrao_de_saida_esperado == 0:
            return self.verifica_se_o_modelo_acertou(saida_do_modelo, padrao_de_saida_esperado)

        elif entrada_1 == 0 and entrada_2 == 0 and padrao_de_saida_esperado == 0:
            return self.verifica_se_o_modelo_acertou(saida_do_modelo, padrao_de_saida_esperado)

    def verifica_se_o_modelo_acertou(self, saida_do_modelo, padrao_de_saida_esperado):
        """ Verifica se o resultado obtido pelo neurônio está correto"""
        if saida_do_modelo == padrao_de_saida_esperado:
            return True
        else:
            return False
