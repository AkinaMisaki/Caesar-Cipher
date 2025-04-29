import os

def clear(): # Função para limpar a tela
    os.system('cls' if os.name == 'nt' else 'clear')

def caesar(): # Função principal

    crypt = "" # Váriável do resultado final

    for char in texto: # Repete o loop até alcançar o fim do texto

        if (ord(char)) == 32: # Checa se o caractére é o espaço, se sim, adiciona no string e começa outro loop FOR
            crypt += " "
            continue

        numlt = ord(char) + rotat # Transforma o número dos caractéres da tabela ASCII e adiciona o número de rotações


        if char.isupper() == True: # Verifica se é uma letra maiúscula e garante que fique dentro do alfabeto de A-Z
            if numlt >= 90:
                numlt -= 26
            elif numlt < 65:
                numlt += 26
        elif char.islower() == True: # Verifica se é uma letra minúscula e garante que fique dentro do alfabeto de a-z
            if numlt >= 123: 
                numlt -= 26
            elif numlt < 97: 
                numlt += 26
        else: # Verifica se é um número, se sim, transforma de volta ao caractére original
            numlt -= rotat
            
        crypt += chr(numlt) # Concatena a letra à string crypt, encriptando ou decriptando a variável
    
    return crypt # Retorna a variável crypt para ser utilizada

while True: # Roda o código até o usuário decidir parar

    texto = input("Insira o texto:\n")
    rotat = int(input("\nInsira quantas posições será movido: (Positivo = Direita; Negativo = Esquerda):\n"))

    resul = caesar()
    print(f"\nResultado:\n{resul}\n")

    saida = input('Aperte enter para continuar ou digite "Sair" para fechar o programa\n')

    if saida.lower() == "sair":
        exit()
    else:
        clear()
        continue

# Exemplo utilizado pelo professor em sala de aula:
# Suhpdwxuh rswlplcdwlrq lv wkh urrw ri doo hylo
# PREMATURE OPTIMIZATION IS THE ROOT OF ALL EVIL

# String teste
# ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz 0123456789 ' ! @ # $ % & * ( ) _ - + =
