# Module warna
from colorama import Fore

# NAME-ERROR:
# Kesalahan ini muncul sebagai respons dari interpreter Python
# ketika kode mencoba menggunakan sebuah nama yang belum dikenal.

# Name Error variable yang belum didefinisikan sebelum digunakan.
x = 10
y = 15 # sesudah di buat
print(Fore.CYAN, y, Fore.RESET) # variable y belum di definisikan.
