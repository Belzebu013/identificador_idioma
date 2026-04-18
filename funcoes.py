import requests
import string

def baixar_texto(url):
    response = requests.get(url)
    return response.text

def limpar_texto(texto):
    texto_format = texto.lower()
    letras_a_z = string.ascii_lowercase
    resultado = ""

    for letra in texto_format:
        if letra in letras_a_z:
            resultado += letra

    return resultado