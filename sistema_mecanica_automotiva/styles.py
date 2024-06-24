from os import system

def titulo(texto_titulo):
    print(f'\n============== <<{texto_titulo}>> ==============')
    
def msg_erro(text):
    print("\n===========================================\n")
    print(text)
    print("\n===========================================\n")
    
def msg_sucesso(text):
    print("\n*******************************************\n")
    print(text)
    print("\n*******************************************\n")

def clear_t():
    # Windows
    # system('clear')

    # Linux
    system('cls')