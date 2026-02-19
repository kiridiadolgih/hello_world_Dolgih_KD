sample_date = "2026-02-19"

files = ["seq1", "seq2.fasta", "seq3.fa", "seq4"]

print(f"Старт обработки файлов за дату: {sample_date}\n")

for name in files:
    if name.endswith((".fasta", ".fa")):
        print(f"Файл '{name}' уже имеет расширение. Оставляем как есть.")
    else:
        new_name = f"{name}_{sample_date}.fasta"
        print(f"Создано новое имя: {new_name}")

print("\nАнализ структуры последовательности:")
seq = "ATATACGCGTA"
for letter in seq:
    print(letter, end="-")
print("Конец последовательности")