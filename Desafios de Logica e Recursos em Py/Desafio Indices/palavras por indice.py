def verifyLenthWords(sentence):
    
    dictionary = {}

    # Separa as palavras
    text = str(sentence).split()

    # Organiza as palavras por ordem decrescente
    text = sorted(text, key=lambda x: len(x), reverse=False)

    # Analisa cada palavra e insere no dicionário
    for word in text:
        lenght = len(word)
        if lenght not in dictionary:
            dictionary[lenght] = []
        if word not in dictionary:
            dictionary[lenght].append(word)
    
    print(dictionary)
        
verifyLenthWords("O rato roeu a roupa do rei de roma")