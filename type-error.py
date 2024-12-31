# Module warna
from colorama import Fore

# TYPE-ERROR:
# Ketika operasi atau fungsi diberikan argumen dengan tipe data
# yang tidak sesuai atau tidak cocok dengan apa yang diharapkan
# oleh operasi atau fungsi tersebut.

# Type Error: operasi dilakukan antara 2 tipe data yang tidak kompatibel.
a = "hello"
b = 5
print(Fore.YELLOW, a + str(b), Fore.RESET) # menambahkan fungsi str.
