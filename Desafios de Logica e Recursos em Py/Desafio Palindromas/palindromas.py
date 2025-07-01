def verifyPalindromas(frase):
    texto = str(frase).lower().split()
    texto = sorted(texto, key=lambda x: len(x), reverse=False)
    
    palindromas = {}

    for palavra in texto:
        if palavra == palavra[::-1]:
            lenght = len(palavra)
            if lenght > 1:
                if lenght not in palindromas: 
                    palindromas[lenght] = []
                if palavra not in palindromas[lenght]:
                    palindromas[lenght].append(palavra)
    
    print(palindromas)

verifyPalindromas("A Ana viu a radar e o ovo no osso")