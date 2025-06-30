import collections

# texto = "O rato roeu a roupa do rei de roma"

# def verifySentence(sentence):
#     counter = collections.Counter(texto)

#     vstr = str(sentence).split()
#     vstr = sorted(vstr, key=lambda word: len(word), reverse=True)[:2]

#     arr = []

#     print(vstr)
    
# verifySentence(texto)


# ----- 2° DESAFIO ------

# def verifyLenthWords(sentence):
    
#     dictionary = {}
#     text = str(sentence).split()
#     text = sorted(text, key=lambda x: len(x), reverse=False)

#     for word in text:
#         lenght = len(word)
#         if lenght not in dictionary:
#             dictionary[lenght] = []
#         if word not in dictionary:
#             dictionary[lenght].append(word)
    
#     print(dictionary)
        
# verifyLenthWords("O rato roeu a roupa do rei de roma")




def verifyPalindromas(frase):
    print(frase)
    texto = str(frase).lower().split() # <- coloca as palavras em caixinhas
    texto = sorted(texto, key=lambda x: len(x), reverse=False)
    poli = {}

    for palavra in texto:
        if palavra == palavra[::-1]:
            lenght = len(palavra)
            if lenght > 1:
                if lenght not in poli: 
                    poli[lenght] = []
                if palavra not in poli[lenght]:
                    poli[lenght].append(palavra)
    
    print(poli)

# verifyPalindromas("A Ana viu a radar e o ovo no osso")

def decorators(func):
    def wrapper(*args, **kwards):
        resultado = func(*args, **kwards)

        indices_nao_eh_isograma = resultado["nao_eh_isograma"].keys()
        indices_eh_isograma = resultado["eh_isograma"].keys()

        for ind in indices_nao_eh_isograma:
            palavras = resultado["nao_eh_isograma"][ind]
            print(f"Essas palavras nao sao isogramas: {palavras}")
        
        for ind in indices_eh_isograma:
            palavras = resultado["eh_isograma"][ind]
            print(f"Essas palavras sao isogramas de {ind} indices: {palavras}")
        
        return resultado
    return wrapper

@decorators
def verifyIsograma(frase):
    sentence = str(frase).lower().split()
    # print(sentence)
    sentence = sorted(sentence, key=lambda s: len(s), reverse=False)

    dictionary = {"nao_eh_isograma":{}, "eh_isograma":{}}

    for palavra in sentence:
        if palavra:
            lenght = len(palavra)
            if len(set(palavra)) == lenght:
                    if lenght not in dictionary["eh_isograma"]:
                        dictionary["eh_isograma"][lenght] = []
                    dictionary["eh_isograma"][lenght].append(palavra)
            else:
                if lenght not in dictionary["nao_eh_isograma"]:
                    dictionary["nao_eh_isograma"][lenght] = []
                dictionary["nao_eh_isograma"][lenght].append(palavra)
    print(f"{dictionary}\n")
    return dictionary

verifyIsograma("amor casa teto ovo mamao bravo radar papel chave")