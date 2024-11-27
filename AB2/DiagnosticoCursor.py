from Dados import buscar_casos, vetorizar_sintomas
import math

def calcular_similaridade(sintomas_paciente_vetor, sintomas_caso_vetor):
    """
    Calcula a similaridade de cossenos entre os vetores de sintomas
    Retorna um valor entre 0 e 1, onde 1 é totalmente similar
    """
    # Produto escalar
    produto = sum(a * b for a, b in zip(sintomas_paciente_vetor, sintomas_caso_vetor))
    
    # Normas dos vetores
    norma_paciente = math.sqrt(sum(x * x for x in sintomas_paciente_vetor))
    norma_caso = math.sqrt(sum(x * x for x in sintomas_caso_vetor))
    
    # Evita divisão por zero
    if norma_paciente == 0 or norma_caso == 0:
        return 0
        
    return produto / (norma_paciente * norma_caso)

def diagnosticar(sintomas_paciente):
    """
    Realiza o diagnóstico baseado nos sintomas do paciente
    Retorna a doença mais provável e seu grau de similaridade
    """
    casos = buscar_casos()
    melhor_similaridade = 0
    diagnostico = None
    
    # Vetoriza os sintomas do paciente
    vetor_paciente = vetorizar_sintomas(sintomas_paciente)
    
    for caso in casos:
        similaridade = calcular_similaridade(vetor_paciente, caso["vetor"])
        if similaridade > melhor_similaridade:
            melhor_similaridade = similaridade
            diagnostico = caso["doenca"]
    
    return diagnostico, melhor_similaridade

def main():
    print("Sistema de Diagnóstico Médico - RBC")
    print("Digite os sintomas separados por vírgula:")
    
    entrada = input().strip().lower()
    sintomas_paciente = [s.strip() for s in entrada.split(",")]
    
    doenca, similaridade = diagnosticar(sintomas_paciente)
    
    print("\nResultado do diagnóstico:")
    print(f"Doença mais provável: {doenca}")
    print(f"Grau de similaridade: {similaridade:.2%}")
    
    if similaridade < 0.3:
        print("\nAtenção: Baixa similaridade encontrada. Recomenda-se consultar um médico.")

if __name__ == "__main__":
    main()
