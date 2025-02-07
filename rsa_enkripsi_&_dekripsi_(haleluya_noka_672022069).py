import math
from google.colab import output

# RSA ENKRIPSI & DEKRIPSI
p = 47
q = 71
n = p * q
toilent_euler = (p-1) * (q-1)

# Public Key
while True:
    output.clear()
    e = int(input("Masukan Kunci Publik (Dengan Syarat Nilai GCD = 1) : "))
    GCD = math.gcd(toilent_euler, e)

    if GCD == 1:
        for a in range(1, 200): # Hasil harus 1 (contoh : 27, 29, 31, dst) [Jangan input PK 1/Jika PK 1 maka enkripsi akan sama dengan dekripsi!]
            d = (toilent_euler * a + 1) / e
            if d.is_integer():
                d_fix = int(d)
                break
        private = d_fix
        break
    else:
        print("\nError! Syarat GCD Nilai Anda Lebih Dari 1\nSilahkan Ulangi!")
        print("\nNILAI GCD ANDA! = ", GCD)
        input("\nEnter untuk lanjut...")

# Input Plaintext
output.clear()
plainteks = input("Plainteks (Dengan Huruf Kapital Semua) : \n")

# Convert ke ASCII
ascii_values = [ord(c) for c in plainteks]

# Enkripsi
print("\nENKRIPSI :")
cipher_text = [(char**e) % n for char in ascii_values]
print(" ".join(map(str, cipher_text)))

# Dekripsi
print("\nDEKRIPSI :")
decrypted_ascii = [(char**private) % n for char in cipher_text]
print(" ".join(map(str, decrypted_ascii)))

# Kembalikan ke Plain Text
print("\nPLAIN TEKS (DEKRIPSI KEMBALI) :")
decrypted_text = "".join(chr(char) for char in decrypted_ascii)
print(decrypted_text)
