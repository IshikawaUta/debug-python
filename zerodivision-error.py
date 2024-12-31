# Module warna
from colorama import Fore

# ZERODIVISION-ERROR:
# terjadi ketika Anda mencoba membagi suatu angka dengan nol (0) dalam Python,
# Operasi pembagian dengan nol adalah operasi matematika yang tidak valid.

# Zero division error: pembagian dengan nol tidak terdefinisikan.
a = 10
b = 5
#result = a/b

# membuat output true(benar) and false(salah).
if b != 0: # jika benar
    result = a/b
    print(Fore.CYAN, result, Fore.RESET)
else: # jika salah
    print(Fore.MAGENTA, "Pembagian tidak boleh dengan nol", Fore.RESET)
