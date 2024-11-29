from collections import defaultdict

# Base de casos com doenças e seus sintomas
casos = [
    {
        "doenca": "Gripe",
        "sintomas": ["febre", "dor de cabeça", "congestão nasal", "dores musculares", "fadiga", "tosse", "calafrios"]
    },
    {
        "doenca": "COVID-19",
        "sintomas": ["febre", "tosse seca", "cansaço", "perda de olfato", "perda de paladar", "dor de garganta", "dificuldade respiratória"]
    },
    {
        "doenca": "Dengue",
        "sintomas": ["febre alta", "dor de cabeça", "dores musculares", "manchas vermelhas", "náusea", "dor nos olhos", "fadiga extrema"]
    },
    {
        "doenca": "Sinusite",
        "sintomas": ["congestão nasal", "dor facial", "pressão no rosto", "secreção nasal", "perda de olfato", "dor de cabeça"]
    },
    {
        "doenca": "Gastroenterite",
        "sintomas": ["náusea", "vômito", "diarreia", "dor abdominal", "febre baixa", "fadiga", "desidratação"]
    },
    {
        "doenca": "Pneumonia",
        "sintomas": ["tosse com catarro", "febre alta", "dificuldade respiratória", "dor no peito", "calafrios", "fadiga"]
    },
    {
        "doenca": "Enxaqueca",
        "sintomas": ["dor de cabeça intensa", "sensibilidade à luz", "náusea", "sensibilidade a sons", "tontura", "visão embaçada"]
    },
    {
        "doenca": "Asma",
        "sintomas": ["falta de ar", "chiado no peito", "tosse seca", "aperto no peito", "dificuldade respiratória"]
    },
    {
        "doenca": "Rinite Alérgica",
        "sintomas": ["espirros", "congestão nasal", "coceira no nariz", "olhos lacrimejantes", "coceira nos olhos"]
    },
    {
        "doenca": "Conjuntivite",
        "sintomas": ["olhos vermelhos", "coceira nos olhos", "secreção ocular", "sensibilidade à luz", "visão embaçada"]
    },
    {
        "doenca": "Amigdalite",
        "sintomas": ["dor de garganta", "febre", "dificuldade para engolir", "gânglios inchados", "mal-estar"]
    },
    {
        "doenca": "Bronquite",
        "sintomas": ["tosse com catarro", "chiado no peito", "falta de ar", "fadiga", "febre baixa"]
    },
    {
        "doenca": "Zika",
        "sintomas": ["febre baixa", "manchas vermelhas", "dor nas articulações", "dor muscular", "olhos vermelhos", "fadiga"]
    },
    {
        "doenca": "Chikungunya",
        "sintomas": ["febre alta", "dor intensa nas articulações", "dor muscular", "dor de cabeça", "manchas vermelhas"]
    },
    {
        "doenca": "Mononucleose",
        "sintomas": ["fadiga extrema", "dor de garganta", "febre", "gânglios inchados", "dor muscular"]
    },
    {
        "doenca": "Labirintite",
        "sintomas": ["tontura", "náusea", "perda de equilíbrio", "zumbido no ouvido", "dor de cabeça"]
    },
    {
        "doenca": "Otite",
        "sintomas": ["dor de ouvido", "febre", "secreção no ouvido", "dificuldade auditiva", "tontura"]
    },
    {
        "doenca": "Herpes Labial",
        "sintomas": ["bolhas nos lábios", "coceira local", "ardência", "dor local", "mal-estar"]
    }
]

def obter_todos_sintomas():
    """Retorna uma lista com todos os sintomas únicos da base"""
    sintomas = set()
    for caso in casos:
        sintomas.update(caso["sintomas"])
    return sorted(list(sintomas))

def vetorizar_sintomas(sintomas_lista):
    """Converte uma lista de sintomas em um vetor binário"""
    todos_sintomas = obter_todos_sintomas()
    vetor = [1 if sintoma in sintomas_lista else 0 for sintoma in todos_sintomas]
    return vetor

def buscar_casos():
    """Retorna a base de casos com vetores binários"""
    casos_vetorizados = []
    for caso in casos:
        casos_vetorizados.append({
            "doenca": caso["doenca"],
            "sintomas": caso["sintomas"],
            "vetor": vetorizar_sintomas(caso["sintomas"])
        })
    return casos_vetorizados
