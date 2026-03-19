#!/bin/bash

echo "--- Анализатор метаболического индекса (ИМТ) ---"
read -p "Введите массу тела (в кг): " weight
read -p "Введите рост (в метрах): " height

if [[ -z "$weight" || -z "$height" ]]; then
    echo "Ошибка: Вес и рост должны быть указаны."
    exit 1
fi
bmi=$(echo "scale=2; $weight / ($height * $height)" | bc)

bmi_int=$(printf "%.0f" $bmi)
echo "-----------------------------------------------"
echo "Ваш индекс массы тела (ИМТ): $bmi_int"

