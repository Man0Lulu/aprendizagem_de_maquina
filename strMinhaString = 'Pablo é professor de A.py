strMinhaString = 'Pablo é professor de ADS'
print(strMinhaString[0])
print(strMinhaString[1:5])
print(strMinhaString[0:5] + '\n' + strMinhaString[6:17])

print(strMinhaString[5:])
print(strMinhaString[:5])
print(strMinhaString[-6])
print(strMinhaString[::])
print(strMinhaString[::2])
strMinhaString = '123456789'

print(strMinhaString[1:7:2])
print(strMinhaString[::-1])

strMinhaString = 'Pablo é professor de ADS'
strMinhaNovaString = strMinhaString[0] + 'aulo'
print(strMinhaNovaString) #vai imprimir paulo

strMinhaString = 'z'
strMinhaString = strMinhaString * 10
print(strMinhaString) #vai imprimir zzzzzzzzzz
print(2+3) #vaim imprimir 5
print('2' + '3') #vai imprimir 23
strMinhaString = 'Pablo é professor de ADS'
strMinhaString = strMinhaString.upper()
print(strMinhaString)#vai imprimir PABLO É PROFESSOR DE ADS
strMinhaString = 'pablo é professor de ADS'
strMinhaString = strMinhaString.split()
print(strMinhaString) #vai imprimmir ['Pablo', 'é', 'professor', 'de', 'ADS']
strMinhaString = 'calabreza, portugesa, marguerita, frango catupiri, bacon com frango, pepperoni'
strMinhaString = strMinhaString.split(',')
print(strMinhaString)

strMeuNome = "Luís nascimento de Sousa"
print(strMeuNome[0:4])
strMeuNome = "Luís, Nascimento, de, Sousa"
strMeuNome = strMeuNome.split(',')
print(strMeuNome)
strMinhaString = 'Pablo'
print(f'Meu nome é: {strMinhaString}.') #vai imprimir: Pablo
strVariavel1 = 'Pablo'
strVariavel2 = 'janeiro'
strVariavel3 = 'Aquario'
print(f'Meu nome é: %s. Nasci em %s e sou do signo de %s'
%(strVariavel1, strVariavel2, strVariavel3))
print('O nome é %s. '%'Pablo')
print('O nome é %r. '%'Pablo')

print('O nome é %s. '%'Pablo/t Coelho')
print('O nome é %s. '%'Pablo/t Coelho')
print('Ponto flutuante: %5.2f' %(13.144)
print('Ponto flutuante: %1.0f' %(13.144)
print('Ponto flutuante: %1.5f' %(13.144)
print('Ponto flutuante: %10.2f' %(13.144)
print('Ponto flutuante: %25.2f' %(13.144)
myTuple = ('a','a','a','b','c','d','e')
print(len(myTuple))
print(myTuple.count('a'))
print(myTuple.index('c'))
