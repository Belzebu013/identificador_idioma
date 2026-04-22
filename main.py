import tkinter as tk
from tkinter import messagebox
import funcoes
import os

# Pasta dos perfis
ARQUIVO_PERFIS = "perfis/perfis.json"

# Função chamada ao clicar no botão.
#   - Lê URL
#   - Processa texto
#   - Carrega perfis
#   - Detecta idioma
def analisar():
    url = entry_url.get().strip()

    if not url:
        messagebox.showwarning("Atenção", "Digite uma URL válida!")
        return

    try:
        texto = funcoes.baixar_texto(url)
        texto = funcoes.limpar_texto(texto)
        freq = funcoes.calcular_frequencia(texto)

        if not os.path.exists(ARQUIVO_PERFIS):
            status_label.config(text="Gerando perfis pela primeira vez...")
            perfis = funcoes.gerar_perfis()
            funcoes.salvar_perfis(perfis)

        perfis = funcoes.carregar_perfis_json()

        idioma, scores = funcoes.comparar_perfis(freq, perfis)
        
        resultado_label.config(text=f"O texto está em: {idioma}, com grau de similaridade {scores[idioma]*100:.2f}%")

    except Exception as e:
        messagebox.showerror("Erro", str(e))


# ---------------- Cria tela pra o usuario digitar a URL ----------------

janela = tk.Tk()
janela.title("Detector de Idioma")
janela.geometry("500x250")

label = tk.Label(janela, text="Digite a URL:", font=("Arial", 12))
label.pack(pady=10)

entry_url = tk.Entry(janela, width=60)
entry_url.pack(pady=5)

btn = tk.Button(janela, text="Analisar idioma", command=analisar)
btn.pack(pady=10)

status_label = tk.Label(janela, text="")
status_label.pack()

resultado_label = tk.Label(janela, text="", font=("Arial", 12, "bold"))
resultado_label.pack(pady=20)

janela.mainloop()