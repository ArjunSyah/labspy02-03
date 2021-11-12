# " labspy02-03 "
# labspy02
## if,elif,else
## Menentukan Nilai Bilangan Terbesar dari 3 Buah Bilangan
### Flowchart 
- Berikut flowchart, untuk menentukan bilangan terbesar dari 3 buah bilangan
![gambar1](ss/ssan1.png)
### Menggunakan statement if, untuk mencari nilai dari 3 buah bilangan
- Disini saya menginisialisasikan "bil1" sebagai bilangan pertama, "bil2" sebagai bilangan kedua, "bil3" sebagai bilangan ketiga.
- Dengan cara statement if untuk "bil1" sebagai bilangan pertamma, elif untuk "bil2" sebagai bilangan kedua, elif untuk "bil3" sebagai bilangan ketiga, dan else jika false atau salah, maksudnya jika inputan user di luar program, dia akan menampilkan ini.
- Berikut program yang saya buat
![gambar2](ss/ssan2.PNG)
 ## Beriikut hasil program yang saya buat
 ### kapan variabel "bil1" dikatakan yang paling besar? variabel "bil1" dikatakan yang paling besar, ketika ia lebih besar dari nilai "bil2", dan juga lebih besar dari niai "bil3"
- Hasil program bilangan pertama yang terbesar
![gambar3](ss/ssan3.PNG)
### Kapan variabel "bil2" dikatakam yang paling besar? variabel "bil2" dikatakan yang paling besar, ketika ia lebih besar dari nilai "bil1", dan juga lebih beesar dari nilai "bil3"
- Hasil program bilangan kedua yang terbesar
![gambar4](ss/ssan4.PNG)
### Kapan variabel "bil3" dikatakam yang paling besar? variabel "bil3" dikatakan yang paling besar, ketika ia lebih besar dari nilai "bil1", dan juga lebih beesar dari nilai "bil2"
- Hasil program bilangan ketiga yang terbesar
![gambar5](ss/ssan5.PNG)
### Selanjutya, bagaimana jika ketiga bilangan sama? nah disini saya menggunakan else, jadi apabila user menginputkan angka yang di luar program ketiga variabel diatas, maka angka tersebut di nyatakan false atau salah 
- Hasil program bilangan apabila ketiga nilai bilangan sama
![gambar6](ss/ssan6.PNG)
## Kelemaham program yang saya buat adalah, jika kita memasukan 2 angka yang sama, maka nilai terakhir dari kedua variabel itu yang terbesar
### Contoh: bil1= 6, bil2= 6, bil3= 5, maka bil2= 6 lah yang dianggap bilangan yang terbesar
# labspy02 selesai
==================================================================================================================================================
# Labspy03
# Latihan 1
## Membuat Prrogram Untuk Menampilkan n Bilangan Acak yang Lebih Kecil dari 0.5
### Flowchart program
- Berikut flowchart program dari program latihan 1, untuk menampilkan n bilangan acak yang lebih kecil dari 0.5
![gambar1](ss/ss1.png)
### Penjelasan alur program 
 > print("Menampilkan n bilangan acak yang lebih kecil dari 0.5") 
-  itu hanya perintah untuk menamilkan judul saja
 > jumlah = int(input("Masukan jumlah n: )) 
-  Adalah perinntah untuk menginputkan nilai n tersebut
 > import random
-  Adalah perintah untuk menginportkan built-in random yang telah tersedia di python
 > for in range (jumlah): 
-  Adalah perintah untuk, i sebagai integer dalam baris jumlah
 > print ("data ke",i+1,"=",(random.uniform(0.1,0.5))) 
-  Adalah perintah untuk menampilkan hasil yang telah di input dengan ketentuan random uniform mulai dari nilai 0.1 sampai 0.5

### Berikut gambaran programnya
![gambar2](ss/ss2.PNG)

### Berikut hasil program yang saya buat
![gambar3](ss/ss3.PNG)
### Latihan 1 selesai
==================================================================================================================================================
# Latihan 2
## Membuat Program Untuk Menampilkan Bilangan Terbesar dari n Buah Data yang Diinputkan
### Flowchart program
- Berikut flowchart program menampilkan bilangan terbesar dari n buah data yang diinputkan
![gambar4](ss/ss4.png)

### Penjelasan alur program
 > print("Menampilkan bilangan terbesar dari n buah data yang diinput") 
- Perintah untuk menampilkan judul program
 > max = 0 
- Adalah perintah untuk pengulangan hingga waktu yang ditentukan
 > a = int(input("Masukan Bilangan: ")) 
- Adalah perintah untuk menginput nilai integer
 > if max < a : 
- Adalah printah untuk tipe data if, atau jika, maksimal lebih kecil dari a atau integer
 > max = a 
- Perintah untuk maksimal sama dengan a atau integer
 > if a==0 :
- Perintah untuk tipe data  if atau jika a sama dengan 0 maka 
 > break 
- Perintah untuk mengakhiri pengulangan, jadi jika menginput nilai 0, maka pengulangan berakhir atau selesai
 > print("bilangan Terbesar adalah: ",max)
- Adalah perintah untuk menampilkan hasil bilangan yang terbesar dari angka-angka yang telah terinput
### Berikut gambaran programnya
![gambar5](ss/ss5.PNG)
### dan berikut hasil dari program, saat dijalankan
![gambar6](ss/ss6.PNG)
### Latihan 2 selesai
==================================================================================================================================================
# Program 1
## Program Untuk Menghitung Laba Investasi
### Flowchart program
- Berikut flowchart dari program menghitung laba investasi
![gambar7](ss/ss7.png)
### Penjelasan alur program 
> print("Laba Investasi")
- Untuk menampilkan judul

> x = int(input("Uang Modal Awal: "))
- untuk menginput nilai x sebagai modal awal

> a = 0*x 
- a adalah bulan pertama, karena bulan pertama belum memiliki laba, jadi masih 0 dikali dengan x nilai uang modal awal

> b = 0*x 
- b adalah bulan kedua, karena bulan kedua belum memiliki laba, jadi nilai x dari uang modal dikali dengan 0

> c = 0.01*x 
- c adalah bulan ketiga, dan sudah memiliki laba 1%, jadi ditulis 0.01 bentuk sederhana dari 1% dikali dengan modal atau uang awal dengan nilai x

> d = 0.01*x 
- d adalah bulan keempat, dan labanya 1%, jadi ditulis 0.01 dikalikan dengan nilai x yang adalah uang awal atau modal

> e = 0.05*x 
- e adalah bulan kelima, dan laba pada bulan kelima sebesar 5%, maka ditulis 0.05 dikalikan dengan nilai x untuk nilai uang awal atau modal

> f = 0.05*x
- f adalah bulan keenam, dan laba pada bulan keenam sebesar 5%, maka ditulis 0.05 dikalikan dengan nilai x untuk nilai uang awal atau modal

> g = 0.05*x 
- g adalah bulan ketujuh, dan laba pada bulan ketujuh sebesar 5%, maka ditulis 0.05 dikalikan dengan nilai x untuk nilai uang awal atau modal

> h = 0.02*x 
- h adalah bulan kedelapan, dan laba pada bulan kedelapan sebesar 2%, maka ditulis 0.02 dikalikan dengan nilai x untuk nilai uang awal atau modal

> y=[a,b,c,d,e,f,g,h] 
- adalah untuk menentukan syarat y yang berisi a,b,c,d,e,f,g,h

> for i in range(len(y)): 
- adalah untuk perulangan data dengan isi data y, dengan menampilkan urutan laba perbulan sesuai range yang di tentukan dengan hasil ke urutan yang diinputkan dari data y

> print("Laba Bulan Ke",i+1 ,"sebesar: ",y[i]) 
- untuk menampilkan hasil laba dari bulan ke 1 sampai terakhir

> z=(a+b+c+d+e+f+g+h) 
- Z untuk data yang berisi hasil penjumlahan laba dari bulan pertama sampai bulan ke delapan

> print("Jumlah Laba Selama 8 Bulan: ",z) 
- menampilkan hasil dari jumlah laba

### Berikut gambaran programnya
![gambar8](ss/ss8.PNG)
### dan berikut hasil dari program setelah dijalankan
![gambar9](ss/ss9.PNG)
## Program 1 selesai
# Sekian Trimakasih