import string as str
import numpy as np

letras = str.ascii_letters
numeros = str.digits
especial = str.punctuation
algarismos = letras + numeros + especial
senha = np.random.choice(list(algarismos),10)
print(''.join(senha))