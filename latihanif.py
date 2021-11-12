print("Program Mencari Bilangan Terbesar dari 3 Bilangan")

bil1 = int(input("Masukan Bilangan pertama:"))
bil2 = int(input("Masukan Bilangan Kedua \t:"))
bil3 = int(input("Masukan Bilangan Ketiga\t:"))

if bil1>bil2>bil3:
    print("Bilangan Pertama Adalah Bilangan Terbesar = ",bil1)
elif bil2>bil3:
    print("Bilangan Kedua Adalah Bilangan terbesar = ",bil2)
elif bil3>bil2:
    print("Bilangan Ketiga Adalah Bilangan Terbesar = ",bil3)
else :
    print("semua bilanngan sama yaitu",bil1)
    
