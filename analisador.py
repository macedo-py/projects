senha = input("Digite sua senha: ")

tem_maiuscula = False
tem_minuscula = False
tem_numero = False

for caractere in senha:
    if caractere.isupper():
        tem_maiuscula = True
    elif caractere.islower():
        tem_minuscula = True
    elif caractere.isdigit():
        tem_numero = True

if tem_maiuscula and tem_minuscula and tem_numero and len(senha) >= 8:
    print("Senha forte!")
else:
    print("Senha fraca! Verifique se ela tem no mínimo 8 caracteres, números e letras maiúsculas/minúsculas.")