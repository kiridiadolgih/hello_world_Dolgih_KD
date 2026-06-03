a = [1, 2, 3]
b = [4, 5, 6]
n = len(a)

scalar = 0

for i in range(n):
    scalar = scalar + a[i] * b[i]

print("Скалярное произведение двух векторов:", scalar)