import tkinter as tk
from tkinter import messagebox
import funcoes
import os

# Pasta e arquivo dos perfis
PASTA_PERFIS = "perfis"
ARQUIVO_PERFIS = os.path.join(PASTA_PERFIS, "perfis.json")


def analisar():
    url = entry_url.get().strip()

    if not url:
        messagebox.showwarning("Atenção", "Digite uma URL válida!")
        return

    try:
        # Garante que a pasta exista
        if not os.path.exists(PASTA_PERFIS):
            os.makedirs(PASTA_PERFIS)

        # Se arquivo não existir, cria perfis primeiro
        if not os.path.exists(ARQUIVO_PERFIS):
            status_label.config(text="Criando perfis pela primeira vez...")
            janela.update()  # atualiza tela imediatamente

            perfis = funcoes.gerar_perfis()
            funcoes.salvar_perfis(perfis)

            status_label.config(text="Perfis criados com sucesso!")
            janela.update()

        # Continua processamento normal
        texto = funcoes.baixar_texto(url)
        texto = funcoes.limpar_texto(texto)
        freq = funcoes.calcular_frequencia(texto)

        perfis = funcoes.carregar_perfis_json()
        idioma, scores = funcoes.comparar_perfis(freq, perfis)

        resultado_label.config(
            text=f"O texto está em: {idioma}, com grau de similaridade {scores[idioma]*100:.2f}%"
        )

        status_label.config(text="")

    except Exception as e:
        messagebox.showerror("Erro", str(e))


# ---------------- Tela ----------------

janela = tk.Tk()
janela.title("Detector de Idioma")
janela.geometry("500x250")

label = tk.Label(janela, text="Digite a URL:", font=("Arial", 12))
label.pack(pady=10)

entry_url = tk.Entry(janela, width=60)
entry_url.pack(pady=5)

btn = tk.Button(janela, text="Analisar idioma", command=analisar)
btn.pack(pady=10)

status_label = tk.Label(janela, text="", fg="blue")
status_label.pack()

resultado_label = tk.Label(janela, text="", font=("Arial", 12, "bold"))
resultado_label.pack(pady=20)

janela.mainloop()