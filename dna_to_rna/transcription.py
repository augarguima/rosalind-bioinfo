import sys

# =========================
# 1. ENTRADA (terminal)
# =========================
# O arquivo de DNA é passado como argumento ao executar o script:
# python script.py input.txt
file_path = sys.argv[1]

# =========================
# 2. LEITURA DO ARQUIVO
# =========================
# Abre o arquivo e lê a sequência de DNA como string única.
# strip() remove quebras de linha e espaços extras.
with open(file_path) as f:
    dna_sequence = f.read().strip()

# =========================
# 3. TRANSCRIÇÃO (DNA → RNA)
# =========================
# Regra biológica:
# T (timina) no DNA vira U (uracila) no RNA.

rna_sequence = "".join(
    "U" if base == "T" else base
    for base in dna_sequence
)

# =========================
# 4. OUTPUT NO TERMINAL
# =========================
print(rna_sequence)

# =========================
# 5. OUTPUT EM ARQUIVO
# =========================
# Cria um arquivo de saída para armazenar o resultado.
# Nome derivado do input para manter rastreabilidade.

output_path = file_path.replace(".txt", "_rna.txt")

with open(output_path, "w") as out:
    out.write(rna_sequence + "\n")
