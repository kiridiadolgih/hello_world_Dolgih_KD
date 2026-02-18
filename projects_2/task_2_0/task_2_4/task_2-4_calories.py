proteins = float(input("Введите массу белков (г): "))
fats = float(input("Введите массу жиров (г): "))
carbs = float(input("Введите массу углеводов (г): "))
calories = (proteins * 4) + (fats * 9) + (carbs * 4)

print(f"Общая калорийность продукта составляет: {calories} ккал")