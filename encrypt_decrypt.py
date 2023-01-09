
alphabet = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7,
            'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14,
            'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21,
            'v':22, 'w':23, 'x':24, 'y':25, 'z':26}

code = {'a':6, 'b':7, 'c':8, 'd':9, 'e':10, 'f':11, 'g':12,
        'h':13, 'i':14, 'j':15, 'k':16, 'l':17, 'm':18, 'n':19,
        'o':20, 'p':21, 'q':22, 'r':23, 's':24, 't':25, 'u':26,
        'v':1, 'w':2, 'x':3, 'y':4, 'z':5}

def decrypt(words):
    ''' '''
    
    org = ''
    counter = 0
    words_lst = words.strip().split()
    
    for word in words_lst:
        
        word = word.strip()
        
        counter += 1
        for char in word:
            org_num = code[char]
            
            for item in alphabet.items():
                if item[1] == org_num:
                    org_char = item[0]
            
            org += org_char
         
        if counter < len(words_lst):
            org += ' '

    return org
            

def encrypt(words):
    ''' '''
    
    enc = ''
    counter = 0
    words_lst = words.strip().split()
    
    for word in words_lst:
        
        word = word.strip()
        
        counter += 1
        for char in word:
            code_num = alphabet[char]
            
            for item in code.items():
                if item[1] == code_num:
                    code_char = item[0]
            
            enc += code_char
         
        if counter < len(words_lst):
            enc += ' '

    return enc