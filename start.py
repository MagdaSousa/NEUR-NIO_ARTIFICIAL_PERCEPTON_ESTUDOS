from treino_do_modelo.treinar_modelo import TreinoModelo
from funcoes_para_ensinar_o_modelo.funcoes_para_testar_modelo import EnsinarModelo

if __name__ == '__main__':
    nome_da_funcao = "FUNÇÃO E"
    # sequencia_para_treino_modelo_binario = EnsinarModelo().sequencial_binario_para_funcao_e()
    numero_da_funcao_desejada = 1
    funcao_para_treino,sequencia_para_treino_modelo_binario = EnsinarModelo().escolher_funcoes(numero_da_funcao_desejada)

    TreinoModelo(nome_da_funcao,
                 sequencia_para_treino_modelo_binario,
                 funcao_para_treino).treinar_modelo(funcao_para_treino)
