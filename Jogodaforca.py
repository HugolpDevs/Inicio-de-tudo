import random

def escolher_palavra():
    palavra = ['Hugo', 'Joao' , 'desafio', 'marmita' , 'cidade' ]
    return random.choice(palavra)

def mostrar_forca(tentativas):
    fases=[
        
        '''
           -----
           |   |
           |   
           |  
           |   
           |  
           -  
        ''',
        '''
           -----
           |   |
           |   O
           |  
           |   
           |  
           -  
        ''',
        '''
           -----
           |   |
           |   O
           |   |
           |   
           |  
           -  
        ''',
        '''
           -----
           |   |
           |   O
           |  /|
           |   
           |  
           -  
        ''',
        '''
           -----
           |   |
           |   O
           |  /|\\
           |   
           |  
           -  
        ''',
        '''
           -----
           |   |
           |   O
           |  /|\\
           |  / 
           |  
           -  
        ''',
        '''
           -----
           |   |
           |   O
           |  /|\\
           |  / \\
           |  
           -  
        '''
    ]
    if tentativas >= len(fases):
        tentativas = len(fases) - 1
    return fases[tentativas]

def jogar_forca():
    palavra = escolher_palavra()
    letras_certas=set()
    letras_erradas=set()
    tentativas= 0
    max_tentativas = 6
    
    print ("Bem vindo ao jogo da forca")
    
    while tentativas < max_tentativas:  
        palavras_ocultas = ''.join([letra if letra in letras_certas else '_' for letra in palavra])
        print(f'palavras:{palavras_ocultas}')
        print(mostrar_forca(tentativas))
    
        if '_' not in palavras_ocultas:
            print('Parabens!!')
            break
    
        tentativa_usuario= input("Adivinhe a letra: ").lower()

        if tentativa_usuario in letras_certas or tentativa_usuario in letras_erradas:
            print('Voce ja tentou essa letra.')
            continue

        if tentativa_usuario in palavra:
            letras_certas.add(tentativa_usuario)
        
        else:
            letras_erradas.add(tentativa_usuario)
            tentativas += 1
    if '_' in palavras_ocultas:
        print('Voce perdeu! A palavra era:', palavra)

jogar_forca()

