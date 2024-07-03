import math
from google.colab import output

while True:
  p = 47
  q = 71
  n = p * q
  toilent_euler = (p-1)*(q-1)

  # Menentukan Kunci Publik
  output.clear()
  e = int(input("Masukan Kunci Publik (Dengan Syarat Nilai GCD = 1) : "))
  GCD = math.gcd(toilent_euler,e)
  if GCD == 1:
    # Untuk Menemukan Nilai Toilent Euler N / Kunci Private
    for a in range(200):
      d = float((toilent_euler*a+1)/e)
      if d%1 == 0:
        d_fix = int(d)
    private = d_fix
    answer_list = []
    break

  else:
    print("\nError! Syarat GCD Nilai Anda Lebih Dari 1\nSilahkan Ulangi!")
    print("\nNILAI GCD ANDA! = ",GCD)
    ulangi_lagi = input("\nEnter untuk lanjut...")
    True

# Input Plainteks Dengan Huruf Kapital Semua
output.clear()
plainteks = input("Plainteks (Dengan Huruf Kapital Semua) : \n")
ascii = [ord(c) for c in plainteks]
concat = ''.join(map(str,ascii))
panjang = len(concat)
print("\nENKRIPSI :")
for i in range(panjang):
  if i%3 == 0:
    a_tambah = i + 3
    hasil = int(concat[i:a_tambah])
    hitung = hasil**e%n
    print(hitung,end='')

print("\n")

# Dekripsi
print("DEKRIPSI :")
for a in range(panjang):
  if a%3 == 0:
    a_tambah = a + 3
    hasil_ = int(concat[a:a_tambah])
    hitung_ = hasil_**e%n
    answer_ = hitung_**private%n
    print(answer_,end='')

print("\n")

# Plainteks Dekripsi Kembali
print("PLAIN TEKS (DEKRIPSI KEMBALI) :")
for a in range(panjang):
  if a%3 == 0:
    a_tambah = a + 3
    hasil_ = int(concat[a:a_tambah])
    hitung_ = hasil_**e%n
    answer_ = hitung_**private%n
    answer_list.append(answer_)

concat_2 = ''.join(map(str, answer_list))
panjang_2 = len(concat_2)
for z in range(panjang_2):
  if z%2 == 0:
    z_tambah = z + 2
    hasil_2 = int(concat_2[z:z_tambah])
    print(chr(hasil_2),end='')
