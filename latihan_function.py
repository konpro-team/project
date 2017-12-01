# function action
def action(kondisi):
	if(kondisi=="Lapar"):
		result = "Harus Makan"
	else:
		result = "Jangan Makan"
	return result


# main progam
hasil = action("Lapar")
print(hasil)
