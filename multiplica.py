#!/usr/bin/python3

num = range(1,11)

for i in num:
	print("Tabla del " + str(i))
	print("-----------")
	
	for j in num:
		result = i * j
		print(str(i)  + " por " + str(j) + " es " + str(result)) 
	
	print("\n")
		
