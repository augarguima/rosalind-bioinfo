# 🧬 Rosalind Bioinformatics Solutions

Este repositório contém minhas soluções para problemas da plataforma Rosalind, com foco em desenvolvimento de habilidades práticas em bioinformática e manipulação de dados biológicos.

O objetivo é evoluir progressivamente do raciocínio básico de programação para a construção de scripts típicos de análise de sequências em bioinformática.

---

# 🚀 Objetivo do projeto

- Praticar lógica de programação aplicada à biologia molecular
- Desenvolver habilidades em Python para análise de sequências biológicas
- Construir base para pipelines de bioinformática (dry lab)
- Documentar evolução técnica de forma estruturada

---

# 🧪 Problemas resolvidos

## 1. DNA Counting

### 📌 Descrição
Contagem das bases nitrogenadas em uma sequência de DNA.

### 🧬 Entrada
Uma string de DNA contendo A, C, G, T

### 📤 Saída
Número de ocorrências de cada base.

### 💡 Conceitos aplicados
- leitura de arquivos via terminal (sys.argv)
- parsing de arquivos de texto
- uso de Counter para contagem eficiente
- manipulação básica de strings

---

## 2. DNA → RNA Transcription

### 📌 Descrição
Transcrição de DNA em RNA substituindo timina (T) por uracila (U).

### 🧬 Regra biológica
DNA → RNA  
T → U

### 📤 Saída
Sequência de RNA correspondente à entrada de DNA.

### 💡 Conceitos aplicados
- leitura de arquivos de entrada
- transformação de strings
- uso de generator expressions
- reconstrução eficiente de strings com join
- introdução a padrões de bioinformática

---

# ⚙️ Como executar os scripts

Exemplo:

python dna_count.py input.txt  
python dna_to_rna.py input.txt  

---

# 📂 Estrutura do repositório

Rosalind_Problem_Solving/  
├── dna_count.py  
├── dna_to_rna.py  
├── rosalind_dna.txt  
├── rosalind_dna_rna.txt  
└── README.md  

---

# 📈 Evolução do projeto

Este repositório será continuamente atualizado conforme avanço na resolução dos problemas da Rosalind, com organização progressiva dos scripts e melhoria na estrutura de código.

---

# 👤 Autor

Augusto Garcia Guimarães, PhD
augarguima@outlook.com

---

# 🧠 Nota

Este projeto representa uma transição prática do raciocínio computacional básico para aplicações em análise de dados biológicos.
