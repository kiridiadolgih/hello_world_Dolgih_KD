seq_list = ["ATATACGCGTA", "CTTCGGNGGA"]
for seq in seq_list:
    print(f"--- Обработка последовательности: {seq} ---")
    for letter in seq:
        print(letter)
    print()
print("Цикл выполнен")