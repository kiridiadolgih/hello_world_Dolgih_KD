total_capsules = int(input("Введите общее количество произведенных капсул: "))
pack_capacity = int(input("Введите вместимость одной упаковки (шт): "))
full_packs = total_capsules // pack_capacity
leftover_capsules = total_capsules % pack_capacity

print(f"\n--- Отчет по фасовке ---")
print(f"Полных упаковок получится: {full_packs}")
print(f"Останется капсул: {leftover_capsules}")