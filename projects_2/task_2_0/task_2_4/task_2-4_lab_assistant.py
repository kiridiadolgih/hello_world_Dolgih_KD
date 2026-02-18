volume = float(input("Введите нужный объем раствора (мл): "))

salt_mass = volume * 0.009

water_volume = volume
with open("recipe.txt", "w", encoding="utf-8") as file:
    file.write("ОТЧЕТ ПО ПРИГОТОВЛЕНИЮ:\n") 
    file.write("-" * 23 + "\n")
    file.write(f"Общий объем: {volume} мл\n")
    file.write(f"Масса соли:  {salt_mass:.2f} г\n")
    file.write(f"Объем воды:  {water_volume} мл\n")

print("Рецепт успешно сохранен в файл recipe.txt")