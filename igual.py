n1=input("Digite o número: ")
if "." in n1:
	n1=float(n1)
else:
	n1=int(n1)
n2=input("Digite o número: ")
if (str(n1).replace(".", "")).isnumeric()==True and (str(n2).replace(".", "")).isnumeric()==True:
	print(str(n1)==str(n2))