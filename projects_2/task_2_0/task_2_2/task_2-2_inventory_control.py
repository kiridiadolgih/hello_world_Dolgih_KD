reagent_name = input("Введите название нового реактива: ")
reagent_quantity = int(input("Введите его количество (целое число): "))

report = (
    f"Реактив {reagent_name} поступил на склад в "
    f"количестве {reagent_quantity} шт."
)

print(report)

with open("inventory.txt", "w", encoding="utf-8") as file:
    file.write(report)