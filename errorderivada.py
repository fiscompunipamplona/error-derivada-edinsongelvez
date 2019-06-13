x = 1
#ς
print("Función:")
print("	 f(x)= x(x-1) ")
print()
print('''Derivada mediante el límite:
			    lim    f(x+ς)-f(x)/ς
			    ς->0         
	 ''')
print()
print("Derivada de la función:")
print("			f'(x)= 2x-1 ")
print()
print('''Forma Analítica:
		 f'(1)= 2(1)-1
		 f'(1)= 1
 ''')
print()
print("Mediante Límites")
print()
y = (((x+10**(-2))*((x+10**(-2))-1))-(x*(x-1)))/10**(-2)
z = x-y
z = z*-1
print("f'(1)= ", y, " [con ς= 10**(-2)] ", " con un error del ",z*100,"%")
y = (((x+10**(-4))*((x+10**(-4))-1))-(x*(x-1)))/10**(-4)
z = x-y
z = z*-1
print("f'(1)= ", y, "[con ς= 10**(-4)] ", " con un error del ",z*100,"%")
y = (((x+10**(-6))*((x+10**(-6))-1))-(x*(x-1)))/10**(-6)
z = x-y
z = z*-1
print("f'(1)= ", y, "[con ς= 10**(-6)] ", " con un error del ",z*100,"%")
y = (((x+10**(-8))*((x+10**(-8))-1))-(x*(x-1)))/10**(-8)
z = x-y
z = z*-1
print("f'(1)= ", y, "[con ς= 10**(-8)] ", " con un error del ",z*100,"%")
y = (((x+10**(-10))*((x+10**(-10))-1))-(x*(x-1)))/10**(-10)
z = x-y
z = z*-1
print("f'(1)= ", y, " [con ς= 10**(-10)] ", "con un error del ",z*100,"%")
y = (((x+10**(-12))*((x+10**(-12))-1))-(x*(x-1)))/10**(-12)
z = x-y
z = z*-1
print("f'(1)= ", y, "[con ς= 10**(-12)] ", "con un error del ",z*100,"%")
y = (((x+10**(-14))*((x+10**(-14))-1))-(x*(x-1)))/10**(-14)
z = x-y
print("f'(1)= ", y, "[con ς= 10**(-14)] ", "con un error del  ",z*100,"%")