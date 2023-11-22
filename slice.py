teclado = "teclado"
print(teclado[2])
print(teclado[4])


# Acessar os ultimos caracteres
teclado2 = "teclado teclado teclado teclado teclado"
print(teclado2[-1])

# não ficar contando os caracteres(buscar o a localização da letra 'L')

teclado3 = 'teclado'
print(teclado3.index('l'))
print(teclado3[teclado3.index('l')])

# Acessando partes de ums string
link = 'facebook.com/devaprender'
print(link[0])
print(link[-1])
print(link[0:5])
print(link[0:])
print(link[-5:])
print(link[5:])
print(link[:-5])

# Acessar a ultima ocorrencia de um caracter
frase = 'Clean Code'
print(frase.rindex('C'))

# Desafio 1 
##encontre o índice do 'o' dentro da váriavel biblioteca
biblioteca = 'Biclioteca'
print(biblioteca.index('o'))

#Desafio2
#usando as palavras

desenvolvimento = 'Desenvolvimento De Aplicações'
#imprima apenas a palávra 'De Aplicações
print(desenvolvimento.rindex('D'))
print(desenvolvimento[16:])
