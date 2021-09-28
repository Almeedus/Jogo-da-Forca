import random
def mensagem_inicio():
    print('*'*15)
    print('Jogo da Forca')
    print('*'*15)

def carregar_palavra_secreta():
    arquivo = open("palavras.txt",'r')
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()

    numero = random.randrange(0,len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta
     
def letras_acertadas_com_(palavra_secreta):
    return ['_' for letra in palavra_secreta]

def chutar():
    chute = input("Qual letra? ")
    chute = chute.strip().upper()
    return chute

def chute_correto(chute, acertos, palavra_chave):
    posicao = 0
    for letra in palavra_chave:
        if chute.upper() == letra.upper():
            acertos[posicao] = letra
        posicao += 1

def vitoria():
    print("="*24)
    print("Parabéns você venceu!")
    print("="*24)

def derrota(palavra_chave):
    print("Eita, você perdeu!")
    print(f"A palavra chave era: {palavra_chave}")

def jogar():
    mensagem_inicio()
    palavra_chave = carregar_palavra_secreta()
    acertos = letras_acertadas_com_(palavra_chave)

    enforcado = False
    acertado = False
    erro = 0

    print("letras acertadas")
    print(acertos)

    while (not enforcado and not acertado):
        chute = chutar()

        if chute in palavra_chave:
            chute_correto(chute, acertos, palavra_chave)
        else:
            erro += 1
        
        enforcado = erro == 3
        acertado = '_' not in acertos
        print("\n",acertos)
        print(f"\nErros: {erro} / 3")

    if acertado:
        vitoria()
    else:
        derrota(palavra_chave)

    print("FIM DE JOGO!")
