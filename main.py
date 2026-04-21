import funcoes 
import sys
import os

sys.stdout.reconfigure(encoding='utf-8')

url = "https://www.academie-francaise.fr"

conteudo_texto = funcoes.baixar_texto(url)
conteudo_texto_limpo = funcoes.limpar_texto(conteudo_texto)
frequencia_letra = funcoes.calcular_frequencia(conteudo_texto_limpo)

ARQUIVO_PERFIS = "perfis.json"

# SÓ GERA SE NÃO EXISTIR
if not os.path.exists(ARQUIVO_PERFIS):
    print("Gerando perfis pela primeira vez...")
    perfis = funcoes.gerar_perfis()
    funcoes.salvar_perfis(perfis)

# SEMPRE CARREGA
perfis = funcoes.carregar_perfis_json()

idioma, scores = funcoes.comparar_perfis(frequencia_letra, perfis)

print(idioma)