#Quiz 1

batas = int(input("Masukan batas: "))
for i in range(1, batas + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

#Quiz 2
angka = []

while True:
    i = int(input("Masukan angka kedalam list. \n(ketik '-999' jika dirasa sudah cukup)\n: "))
    if i == -999:
        break
    angka.append(i)

print(f"Final list anda adalah {angka} ")

if len(angka) == 0:
    print("List anda kosong. Tolong isi beberapa")
else:
    angka_terbesar = angka[0]
    for i in angka:
        if i > angka_terbesar:
            angka_terbesar = i
    print(f"angka_terbesar dalam list anda adalah {angka_terbesar}")
