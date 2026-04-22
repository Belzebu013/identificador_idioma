# 🌍 Detector de Idioma por Frequência de Letras

Este projeto identifica automaticamente o idioma de um texto a partir de uma URL, utilizando análise estatística baseada na frequência de letras e similaridade de cosseno.

---

## 🚀 Como funciona

O sistema segue os seguintes passos:

1. Baixa o conteúdo textual de uma página web
2. Remove elementos irrelevantes (scripts, menus, rodapés, etc.)
3. Limpa o texto:

   * Converte para minúsculas
   * Remove acentos
   * Mantém apenas letras de **a–z**
4. Calcula a frequência relativa de cada letra
5. Compara com perfis de idiomas previamente gerados
6. Retorna o idioma mais provável com base na similaridade

---

## 🧠 Técnica utilizada

O método principal é a **similaridade de cosseno**:

```
sim(A, B) = (A · B) / (||A|| * ||B||)
```

Onde:

* A = vetor de frequência do texto analisado
* B = vetor de frequência do idioma

---

## 📦 Requisitos

Instale as dependências necessárias:

```bash
pip install requests beautifulsoup4
```

---

## ▶️ Como executar

```bash
python main.py
```

Ao executar:

* Uma interface gráfica será aberta
* Digite uma URL
* Clique em **"Analisar idioma"**

---

## 🧠 Primeira execução

Na primeira vez que rodar o sistema:

* Os perfis de idioma serão gerados automaticamente
* Serão salvos no arquivo:

```
perfis/perfis.json
```

Nas próximas execuções:

* Os perfis serão carregados automaticamente (sem precisar regenerar)

---

## 🌐 Exemplos de URLs para teste

Use páginas com bastante texto:

* https://www.spiegel.de → Alemão
* https://www.nytimes.com → Inglês
* https://g1.globo.com → Português
* https://elpais.com/america/ → Espanhol
* https://www.lemonde.fr → Francês

---

## 📁 Estrutura do projeto

```
identificador_idioma/
│
├── main.py              # Interface gráfica (Tkinter)
├── funcoes.py           # Lógica do sistema
├── perfis/
│   └── perfis.json      # Perfis dos idiomas (gerado automaticamente)
└── README.md
```

---

## ⚙️ Principais funções

### `baixar_texto(url)`

* Faz o download da página
* Extrai apenas o texto relevante

### `limpar_texto(texto)`

* Remove acentos
* Mantém apenas letras (a-z)

### `calcular_frequencia(texto)`

* Calcula a frequência de cada letra

### `gerar_perfis()`

* Baixa várias páginas por idioma
* Cria o perfil estatístico de cada idioma

### `comparar_perfis(freq_texto, perfis)`

* Compara o texto com cada idioma
* Retorna o mais semelhante

---

## ⚠️ Limitações

* Funciona melhor com textos grandes
* Pode errar em textos curtos
* Idiomas parecidos (Português/Espanhol) podem confundir
* Ignora acentos (o que reduz precisão em alguns casos)
