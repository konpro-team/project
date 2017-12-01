# fungsi luas lingkaran
def luas_lingkaran(r):
	luas = phi*(r**2)
	return luas

# fungsi keliling lingkaran
def keliling_lingkaran(r):
	keliling = 2*phi*r
	return keliling

# main program
phi = 3.14
r = 8
l = luas_lingkaran(r)
k = keliling_lingkaran(r)
print("Luas Lingkaran adalah : %.2f"%(l))
print("Keliling Lingkaran adalah : %.2f"%(k))
