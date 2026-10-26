nome = ""
nota_primeiro_trimestre=0.0
aprovado = False
resultado=""
continuar=True

nome= input("escreva o nome do aluno:")

while continuar:
    try:
        nota_primeiro_trimestre = float(input("digite o valor da nota do 1 trimestre: "))
        break
    
    except ValueError:
        print("\nreescreva, carácter não aceito, digite APENAS NÚMEROS EM DECIMAL\n")
    
if nota_primeiro_trimestre < 6.0:
    aprovado = False
   
    
elif nota_primeiro_trimestre >6.0:
        aprovado= True
    
if aprovado:
    resultado="aprovado"
elif not aprovado:
    resultado="não aprovado"

print("\nresumo do aluno:\n", nome,",", resultado)
