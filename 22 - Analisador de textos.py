nome = input('Digite seu nome completo: ').strip()
print(nome.upper())
print(nome.lower())
print(f'Seu nome tem {len(nome)-nome.count(' ')} letras')
separa = nome.split()
print(separa[0], len(separa[0]))