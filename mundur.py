hitung_dari = int(input("hitung mundur dari:"))
hitung_sampai = int(input("hitung mundur sampai:"))
for i in range(hitung_dari, hitung_sampai - 1, -1):
    print(i)
if hitung_sampai > hitung_dari:
    print("belajar lagi dek")
