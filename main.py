import funcoes 

# Pega o conteudo de texto da pagina
url = "https://github.com/"
conteudo_texto = funcoes.baixar_texto(url)

# Limpa o conteudo mantendo apenas as letras
conteudo_texto_limpo = funcoes.limpar_texto(conteudo_texto)

# print(conteudo_texto)
print(conteudo_texto_limpo)