print("Pirmais uzdevums!!!")
a = float(input("Ievadi pirmo skaitli: "))
b = float(input("Ievadi otro skaitli: "))
c = float(input("Ievadi trešo skaitli: "))
print("Summa:", a + b + c)
print("Vidējais:", (a + b + c) / 3)

print("Otrais uzdevums!!!")
a = float(input("Ievadi pirmo skaitli: "))
b = float(input("Ievadi otro skaitli: "))
c = float(input("Ievadi trešo skaitli: "))
print("Lielākais skaitlis:", max(a, b, c))

print("Trešais uzdevums!!!")
n = int(input("Ievadi n: "))
summa = 0
for i in range(1, n + 1):
    summa += i
print("Summa:", summa)

print("Ceturtais uzdevums!!!")
atzimes = [8, 6, 9, 7, 5, 10, 7]
print("Atzīmju skaits:", len(atzimes))
print("Vidējā atzīme:", sum(atzimes) / len(atzimes))
print("Lielākā atzīme:", max(atzimes))
print("Atzīmes 7 vai lielākas:", sum(1 for a in atzimes if a >= 7))

print("Piektais uzdevums!!!")
def cena_ar_atlaidi(cena, atlaide=10):
    return cena * (100 - atlaide) / 100
print(cena_ar_atlaidi(100))
print(cena_ar_atlaidi(100, 25))25