
# Apenas mostrar a mensagem 
with open("mensagem.txt", "r",encoding ="utf-8") as arquivo:
    mensagem = arquivo.readlines()
    print(mensagem)

    for linha in mensagem: 
        if "faturamento" in linha:
            print(linha)

    for linha in mensagem:
        if "Qualquer" in linha:
            print(linha)


# Criar e substituir uma mensagem 
with open("nova_senha.txt", "w", encoding="utf-8") as arquivo:
    senha = arquivo.write("cerutti")
    print(senha)

# Adicionar novos textos 
with open("email.txt", "a" , encoding="utf-8") as arquivo:
    email = arquivo.write("\nalice.sturlese.siveira@gmail.com")
    print(email)

