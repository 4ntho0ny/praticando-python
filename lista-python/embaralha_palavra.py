import random

def embaralha_palavra(palavra):
    lenght = len(palavra)
    palavra_embr = "".join(random.sample(palavra, lenght))
    return palavra_embr

print(embaralha_palavra("asdfg"))