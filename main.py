salarios = []
contapessoa = 0
impostofaixa2 = 0
impostofaixa3 = 0
impostofaixa4 = 0
impostofaixa5 = 0

numero_pessoas = int(input("Digite o número de pessoas: "))

while contapessoa < numero_pessoas:
  contapessoa += 1
  salarios.append(float(input("Digite o salário: ")))

for salario in salarios:
  if salario > 3000.00 and salario <= 4000.00:
    salario -= 3000.00
    impostofaixa2 = salario * 0.075
    print(f"R$ {impostofaixa2:.2f}")
  elif salario > 4000.00 and salario <= 6000.00:
    salario -= 3000.00
    impostofaixa2 = 1000 * 0.075
    salario -= 1000
    impostofaixa3 = salario * 0.15
    print(f"R$ {impostofaixa2 + impostofaixa3:.2f}")
  elif salario > 6000.00 and salario <= 7500.00:
    salario -= 3000.00
    impostofaixa2 = 1000 * 0.075
    salario -= 1000
    impostofaixa3 = salario * 0.15
    salario -= 2000
    impostofaixa4 = salario * 0.225
    print(f"R$ {impostofaixa2 + impostofaixa3 + impostofaixa4:.2f}")
  elif salario > 7500.00:
    salario -= 3000.00
    impostofaixa2 = 1000 * 0.075
    salario -= 1000
    impostofaixa3 = salario * 0.15
    salario -= 2000
    impostofaixa4 = salario * 0.225
    salario -= 1500.00
    impostofaixa5 = salario * 0.28
    print(f"R$ {impostofaixa2 + impostofaixa3 + impostofaixa4 + impostofaixa5:.2f}")
  else:
    print("ISENTO")