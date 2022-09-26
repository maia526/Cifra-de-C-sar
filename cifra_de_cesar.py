abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def gerar_alfabeto(chave):
    abc2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    if chave < 27:
        muda = abc[0:chave]
    else:
        x = chave / 26
        muda = abc[0:chave - (x*26)]

    for i in muda:
        abc2.remove(i)
    for i in muda:
        abc2.append(i)
    return abc2

def pegar_chave():
    chave = int(input("Digite a chave (numeros positivos maiores que 0): "))

    if chave >= 0:
        return chave
    else:
        return chave * (-1)

def pegar_frase():
    frase = input("Digite a frase: ")
    return frase

def separar_frase(frase):
    frase_separada=[]

    for i in frase:
        frase_separada.append(i)
    return frase_separada

def trocar_letras(frase_separada, abc2):
    for i in range(len(frase_separada)):
        for j in range(len(abc)):
            if frase_separada[i] != ' ': 
                if frase_separada[i] == abc[j]:
                    frase_separada[i] = abc2[j + 1]
                    break

def destrocar_letras(frase_separada, abc2):
    for i in range(len(frase_separada)):
        for j in range(len(abc)):
            if frase_separada[i] != ' ': 
                if frase_separada[i] == abc2[j]:
                    frase_separada[i] = abc[j - 1]
                    break

def imprimir_frase(frase_separada):
    for letter in frase_separada:
        print(letter, end='')

def decodificar():
    chave = pegar_chave()
    abc2 = gerar_alfabeto(chave)
    frase = pegar_frase()
    frase_separada = separar_frase(frase)
    destrocar_letras(frase_separada, abc2)
    imprimir_frase(frase_separada)

def codificar():
    chave = pegar_chave()
    abc2 = gerar_alfabeto(chave)
    frase = pegar_frase()
    frase_separada = separar_frase(frase)
    trocar_letras(frase_separada, abc2)
    imprimir_frase(frase_separada)


ativo = True
while(ativo):
    modo = input("Deseja codificar ou descodificar uma frase? c/d: ")
    modo = modo.lower()
    if modo == 'c':
        codificar()
        
        confirma = input("\nDeseja continuar? s/n: ")
        if confirma == 'n':
            ativo = False
    if modo == 'd':
        decodificar()

        confirma = input("\nDeseja continuar? s/n: ")
        if confirma == 'n':
            ativo = False
