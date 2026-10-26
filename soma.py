continua=True

def soma(num1, num2):
    return (num1 + num2)
while continua:
    try:
     num1 = float(input('entre com o primeiro numero: '))
     num2 = float(input('entre com o segundo numero'))
     break
    except ValueError:
     print("VALOR NÃO CORRESPONDE! digite novamente")

print(f'a soma de {num1} mais {num2} é {soma(num1, num2)}')
