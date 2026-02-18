weight = float(input("Введите ваш вес (кг): 60"))
height_cm = float(input("Введите ваш рост (см): 174"))
height_m = height_cm / 100

bmi = weight / (height_m ** 2)
print("\n--- Отчет о физических показателях ---")
print(f"Ваш рост:\t{height_cm} см")
print(f"Ваш вес:\t{weight} кг")
print(f"Ваш ИМТ:\t{bmi:.2f}")