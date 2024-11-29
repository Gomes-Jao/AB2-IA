from DadosGpt4 import doencas
from collections import Counter
import math

def calcular_similaridade_cosseno(vetor1, vetor2):
    # Calcular o produto escalar
    produto_escalar = sum(a * b for a, b in zip(vetor1, vetor2))
    
    # Calcular a magnitude dos vetores
    magnitude_vetor1 = math.sqrt(sum(a * a for a in vetor1))
    magnitude_vetor2 = math.sqrt(sum(b * b for b in vetor2))
    
    # Evitar divisão por zero
    if magnitude_vetor1 == 0 or magnitude_vetor2 == 0:
        return 0.0
    
    # Calcular a similaridade de cosseno
    return produto_escalar / (magnitude_vetor1 * magnitude_vetor2)

def diagnosticar(sintomas_usuario):
    # Criar um conjunto de todos os sintomas possíveis
    todos_sintomas = set(sintoma for sintomas in doencas.values() for sintoma in sintomas)
    
    # Criar vetor de sintomas do usuário
    vetor_usuario = [1 if sintoma in sintomas_usuario else 0 for sintoma in todos_sintomas]
    
    doenca_mais_provavel = None
    maior_similaridade = 0

    for doenca, sintomas in doencas.items():
        # Criar vetor de sintomas da doença
        vetor_doenca = [1 if sintoma in sintomas else 0 for sintoma in todos_sintomas]
        
        # Calcular similaridade de cosseno
        similaridade = calcular_similaridade_cosseno(vetor_usuario, vetor_doenca)
        
        if similaridade > maior_similaridade:
            maior_similaridade = similaridade
            doenca_mais_provavel = doenca

    return doenca_mais_provavel

# Exemplo de uso
sintomas_usuario = ["febre", "tosse", "fadiga"]
doenca = diagnosticar(sintomas_usuario)
print(f"A doença mais provável é: {doenca}")
