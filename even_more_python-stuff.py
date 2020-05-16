poopoo = open("newfile.txt","r")
print(poopoo.read())
poopoo.close()

poopoo = open("newfile.txt", 'w')
poopoo.write("byebye poopoo")
poopoo.close()

with open("newfile.txt", "r") as poop:
	print(poop.read())
