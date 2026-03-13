import hashlib


user1_nome = "ana"
user1_hash = "12313a3d28f802e3a22b07d2e01c6dcf"

user2_nome = "bia"
user2_hash = "f8dbbbdb3b80b4f170a8272978f579eb"

user3_nome = "caio"
user3_hash = "5fa9db2e335ef69a4eeb9fe7974d61f4"

user4_nome = "dani"
user4_hash = "c303183db8ccee2fb0a2f5ca6c030f68"

user5_nome = "rei"
user5_hash = "bea0184aac2ef216c834b3e24a88c38e"


login = input("Digite seu usuário: ")
senha = input("Digite sua senha: ")

hash_senha_digitada = hashlib.md5(senha.encode()).hexdigest()

acesso_concedido = False

if login == user1_nome and hash_senha_digitada == user1_hash:
    acesso_concedido = True
elif login == user2_nome and hash_senha_digitada == user2_hash:
    acesso_concedido = True
elif login == user3_nome and hash_senha_digitada == user3_hash:
    acesso_concedido = True
elif login == user4_nome and hash_senha_digitada == user4_hash:
    acesso_concedido = True
elif login == user5_nome and hash_senha_digitada == user5_hash:
    acesso_concedido = True

if acesso_concedido:
    print(print("\nAcesso Concedido! Bem-vindo(a), " + login + "!"))
else:
    print("\nAcesso Negado! Usuário ou senha incorretos.")

