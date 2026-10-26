ano_nascimento=0
idade=0
continuar = True
resultado = 0
ano_atual=0
idade=0

while continuar:
    try:
        ano_nascimento = int(input("digite o ano de nascimento:\n"))
        break
        
    except ValueError:
        print("reescreva, utilize APENAS NÚMEROS INTEIROS")
        
while continuar:
    try:
        ano_atual = int(input("digite o ano atual:\n"))
        break
        
    except ValueError:
        print("reescreva, utilize APENAS NÚMEROS INTEIROS")        

def somar(ano_atual, ano_nascimento):
    idade = ano_atual - ano_nascimento
    return idade

idade = somar(ano_atual, ano_nascimento)
print("a idade é", idade)
        
        