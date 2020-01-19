i = 0
while i<1:
	x = int(input("Write your first number: "))
	y = int(input("Write your second number: "))
	oper = ["+","-","*","/"]
	op = str(input("Choose operator from (+,-,*,/): "))
	if op == "+":
		z = x+y
		print(z)
	elif op == "-":
		z = x-y
		print(z)
	elif op == "*":
		z = x*y
		print(z)
	elif op == "/":
		z = x/y
		print(z)
	else :
		print("Unknown operator try againe")
	a = str(input("""If you want to exit enter "E"/n or "C" """))
	if a == "E":
		break
	elif a == "C":
		continue
exit(0)

	

