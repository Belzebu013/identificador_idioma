import requests, unicodedata, string, math, json
import pandas as pd
from bs4 import BeautifulSoup
from collections import Counter

# URL's para baixar o conteudo do site e ser usado para a criação dos perfis
URLS = {
   "Alemão": [
        "https://www.dw.com/de/deutsch-lernen/top-themen/s-8031",
        "https://www.tagesschau.de/",
        "https://www.spiegel.de/",
        "https://de.wikisource.org/wiki/Hauptseite",
        "https://de.wikipedia.org/wiki/Berlin"
    ],
    "Português": [
        "https://g1.globo.com/",
        "https://www.uol.com.br/",
        "https://pt.wikipedia.org/wiki/Língua_portuguesa",
        "https://www.publico.pt/",
        "https://www.rtp.pt/"
    ],
    "Espanhol": [
        "https://elpais.com/",
        "https://www.elmundo.es/",
        "https://es.wikipedia.org/wiki/Idioma_español",
        "https://www.bbc.com/mundo",
        "https://www.lanacion.com.ar/"
    ],
    "Frances": [
        "https://www.lemonde.fr/",
        "https://www.lefigaro.fr/",
        "https://fr.wikipedia.org/wiki/Langue_française",
        "https://www.france24.com/fr/",
        "https://www.rfi.fr/fr/"
    ],
    "Inglês": [
        "https://www.bbc.com/news",
        "https://www.theguardian.com/international",
        "https://en.wikipedia.org/wiki/English_language",
        "https://www.nytimes.com/",
        "https://www.cnn.com/"
    ]
}

# Baixa o conteúdo HTML da página e extrai o texto visível.
# Remove elementos como scripts, estilos e navegação.
def baixar_texto(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    for tag in soup(["script", "style", "nav", "footer", "header"]):
        tag.decompose()

    content = soup.find("div", {"id": "bodyContent"})
    return content.get_text(" ") if content else soup.get_text(" ")

# - Converte para minúsculo
# - Remove acentos
# - Mantém apenas letras de 'a' a 'z'
def limpar_texto(texto):
    import unicodedata

    texto = texto.lower()
    texto = unicodedata.normalize('NFD', texto)
    texto = ''.join(c for c in texto if unicodedata.category(c) != 'Mn')

    return ''.join(c for c in texto if 'a' <= c <= 'z')

# Calcula a frequência relativa de cada letra (a-z)
def calcular_frequencia(texto_formatato):
    if len(texto_formatato) == 0:
        return {l: 0 for l in string.ascii_lowercase}

    contagem = Counter(texto_formatato)
    total = len(texto_formatato)

    return {
        letra: contagem[letra] / total if total > 0 else 0
        for letra in string.ascii_lowercase
    }

# =============================
# GERA PERFIS
# =============================

# Para cada idioma:
# - Baixa várias páginas
# - Junta os textos
# - Calcula frequência de letras
def gerar_perfis():
    perfis = {}

    for idioma, urls in URLS.items():
        textos = []

        for url in urls:
            t = baixar_texto(url)
            textos.append(t)

        texto_total = " ".join(textos)

        # 🔥 ESSA PARTE ESTAVA FALTANDO
        texto_limpo = limpar_texto(texto_total)
        freq = calcular_frequencia(texto_limpo)

        perfis[idioma] = freq

    return perfis

# =============================
# SALVAR
# =============================

def salvar_perfis(perfis, arquivo="perfis/perfis.json"):
    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(perfis, f, indent=4)

def carregar_perfis_json():
    with open("perfis/perfis.json", "r", encoding="utf-8") as f:
        return json.load(f)

# Compara o texto com cada idioma usando similaridade de cosseno
# Retorna o idioma mais provável
def comparar_perfis(freq_texto, perfis):
    resultados = {}

    for idioma, perfil in perfis.items():

        produto = 0
        norma_texto = 0
        norma_idioma = 0

        for letra in string.ascii_lowercase:
            freq_t = freq_texto.get(letra, 0)
            freq_i = perfil.get(letra, 0)

            produto += freq_t * freq_i
            norma_texto += freq_t ** 2
            norma_idioma += freq_i ** 2

        if norma_texto > 0 and norma_idioma > 0:
            similaridade = produto / (math.sqrt(norma_texto) * math.sqrt(norma_idioma))
        else:
            similaridade = 0

        resultados[idioma] = similaridade

    melhor = max(resultados, key=resultados.get)

    return melhor, resultados