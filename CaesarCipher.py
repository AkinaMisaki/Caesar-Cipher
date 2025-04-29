alfab = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' # Variável referência do alfabeto
crypt = "" # Variável do resultado final
texto = input("Insira o texto: ")
rotat = int(input("Insira quantas posições será movido: (Positivo = Direita; Negativo = Esquerda): "))

for x in range(0, len(texto)): # Repete o loop até alcançar o fim do texto

    texlw = texto.lower() # Transforma o número em minúsculo para ter consistência de valores da tabela ASCII

    if (ord(texlw[x])) == 32: # Checa se o caractére é o espaço, se sim, adiciona no string e começa outro loop FOR
        letra = " " 
        crypt += letra 
        continue

    numlt = ord(texlw[x]) - 97 # Transforma o número dos caractéres da tabela ASCII para 0-25 (1-26)
    numlt += rotat # Adiciona a quantidade de rotações/movimentações da cifra ao número

    if numlt >= 26: #Verifica se o programa está tentando ler algo após de Z, se sim, volta para A
        numlt -= 26
    elif numlt < 0: #Verifica se o programa está tentando ler algo antes de A, se sim, vai para Z
        numlt += 26

    letra = alfab[numlt] # Coloca o caractére equivalente do número na variável letra
    crypt += letra # Concatena a letra à string crypt, encriptando ou decriptando a variável

print(crypt)

# Exemplo utilizado pelo professor em sala de aula:
# Suhpdwxuh rswlplcdwlrq lv wkh urrw ri doo hylo
# PREMATURE OPTIMIZATION IS THE ROOT OF ALL EVIL
