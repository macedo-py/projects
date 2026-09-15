<<<<<<< HEAD
=======
SENHAS_COMUNS =["12345678", "password", "qwertyuiop", "abcd1234", "123456789"]

>>>>>>> 1501169 (Ajuste e adição de coisas no código)
senha = input("Digite sua senha: ")

tem_maiuscula = False
tem_minuscula = False
tem_numero = False
tem_caractere = False
<<<<<<< HEAD

for caractere in senha:
    if caractere.isupper():
        tem_maiuscula = True
    elif caractere.islower():
        tem_minuscula = True
    elif caractere.isdigit():
        tem_numero = True
    elif not caractere.isalnum():
        tem_caractere = True

if tem_maiuscula and tem_minuscula and tem_numero and tem_caractere and len(senha) >= 8:
    print("Senha forte! Aprovada.")
else:
    print("Senha fraca! Verifique se ela tem no mínimo 8 caracteres, números e letras maiúsculas/minúsculas.")
=======
tem_especial = False

caracteres_especiais = "!@#$%^&*()_+-=[]{}|;:,.<>?"

if senha.lower() in SENHAS_COMUNS:
    print("Senha comum! Escolha uma senha mais segura.")
else:

    for caractere in senha:
        if caractere.isupper():
            tem_maiuscula = True
        elif caractere.islower():
            tem_minuscula = True
        elif caractere.isdigit():
            tem_numero = True
        elif caractere in caracteres_especiais:
            tem_especial = True

pontos = 0
if len(senha) >= 8: pontos += 1
if len(senha) >= 12: pontos += 1 
if tem_maiuscula: pontos += 1
if tem_minuscula: pontos += 1
if tem_numero: pontos += 1
if tem_especial: pontos += 1

print(f"Pontuação da senha: {pontos}/6")

if pontos <= 2:
    print("SENHA FRACA")
elif pontos <= 4:
    print("SENHA MÉDIA")
elif pontos <= 5:
    print("SENHA FORTE")
else:
    print("SENHA MUITO FORTE (Excelente!)")

if pontos < 6:
    print("\n----Sugestões para melhorar sua senha:")
    if len(senha) < 8:
        print("- Sua senha deve ter pelo menos 8 caracteres (ideal: 12 ou mais).")
    if not tem_maiuscula:
        print("- Sua senha deve conter pelo menos uma letra maiúscula.")
    if not tem_minuscula:
        print("- Sua senha deve conter pelo menos uma letra minúscula.")
    if not tem_numero:
        print("- Sua senha deve conter pelo menos um número.")
    if not tem_especial:
        print("- Sua senha deve conter pelo menos um caractere especial.")
>>>>>>> 1501169 (Ajuste e adição de coisas no código)
