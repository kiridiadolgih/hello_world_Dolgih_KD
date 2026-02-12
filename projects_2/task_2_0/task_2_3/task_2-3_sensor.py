operator_name = input("Введите имя оператора: ")
pressure_value = input("Введите текущее значение датчика давления: ")

with open("sensor_log.txt", "w", encoding="utf-8") as file:
    file.write("ОПЕРАТОР\tЗНАЧЕНИЕ\n")
    file.write(f"{operator_name}\t{pressure_value}\n")

print("Данные успешно сохранены в sensor_log.txt")