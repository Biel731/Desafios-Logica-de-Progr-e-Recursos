# Decorators: adicionam uma funcionalidade à função sem a necessidade de alterar diretamente seu conteúdo.

def decorators(func):
    def wrapper(*args, **kwards):
        resultado = func(*args, **kwards)

        indices_nao_isograma = resultado["nao_isograma"].keys()
        indices_isograma = resultado["isograma"].keys()

        for ind in indices_nao_isograma:
            palavras = resultado["nao_isograma"][ind]
            print(f"Essas palavras nao sao isogramas: {palavras}")
        
        for ind in indices_isograma:
            palavras = resultado["isograma"][ind]
            print(f"Essas palavras sao isogramas de {ind} indices: {palavras}")
        
        return resultado
    return wrapper

@decorators
def verifyIsograma(frase):
    sentence = str(frase).lower().split()
    sentence = sorted(sentence, key=lambda s: len(s), reverse=False)

    dictionary = {"nao_isograma":{}, "isograma":{}}

    for palavra in sentence:
        if palavra:
            lenght = len(palavra)
            if len(set(palavra)) == lenght:
                    if lenght not in dictionary["isograma"]:
                        dictionary["isograma"][lenght] = []
                    dictionary["isograma"][lenght].append(palavra)
            else:
                if lenght not in dictionary["nao_isograma"]:
                    dictionary["nao_isograma"][lenght] = []
                dictionary["nao_isograma"][lenght].append(palavra)
    print(f"{dictionary}\n")
    return dictionary

verifyIsograma("amor casa teto ovo mamao bravo radar papel chave colher")