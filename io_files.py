# program baca dan menulis file
file = open("data.txt","r")
print("=== Membaca secara keseluruhan ===")
print(file.read())
print("----------------------------------\n")

file = open("data.txt","r")
print("=== Membaca berdasarkan baris ===")
print(file.readline())
print("----------------------------------\n")
print(file.readline())

file = open("data.txt","r")
print("=== Membaca berdasarkan baris menggunakan perulangan ===")
for data in file:
	print(data)
print("----------------------------------\n")

file = open("data.txt","w")
print("=== Menuliskan data kedalam file ===")
result = file.write("Bahasa Pemrograman Python")
print(result)

print("=== Menuliskan tuple kedalam file ===")
tuple = (1, "bahasa")
data = str(tuple)
result = file.write(data)
print(result)
print("----------------------------------\n")

file = open("data.txt","a+")
print("=== menambahkan data kedalam file tanpa harus menghapus ===")
result = file.write("data lagi")
print(result)
print("----------------------------------\n")


