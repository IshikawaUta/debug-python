# Module warna
from colorama import Fore

# INDEX-ERROR:
# terjadi ketika Anda mencoba mengakses elemen
# di luar batas indeks yang valid dalam sebuah list, tuple, atau string.
# Indeks yang valid biasanya dimulai dari 0 hingga panjang koleksi dikurangi satu.

# Index Error: mengakses indeks yang gada dalam daftar list.
numbers = [1, 2, 3, 4, 5, 6] # sebelum di ubah numbers = [1, 2, 3, 4, 5]
#print(numbers [5])

# membuat output true(benar) and false(salah).
if len(numbers) > 5: # jika benar
    print(Fore.BLUE, numbers [5], Fore.RESET)
else: # jika salah
    print(Fore.RED, "Index tidak ditemukan", Fore.RESET)
