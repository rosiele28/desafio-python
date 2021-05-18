def menu():
  print('======================================')
  print('====Controle de folha de pagamento====')
  print('======================================')
  print("escolha a opção desejada:")
  print("1-Cadastrar funcionário")
  print("2-Imprimir contracheque")
  print('Digite 3 para fechar o programa')

def cadastro_funcionario(funcionarios):
  nome = input("Cadastre o nome do funcionario: ")
  salario = float(input("Qual será o salario bruto de {} ? ".format(nome)))
  funcionarios.append((nome, salario)) #Adiciona a lista criada com o cadastro da pessoa dentro da lista

def contracheque(func):
  funcionario = buscar_funcionario(func)
  print("FUNCIONARIO: {}".format(funcionario[0]))
  salario = funcionario[1]
  print("SALARIO BRUTO R$ %s" % format_number(salario))
  print("INSS: R$ %s" % format_number(inss(salario)))
  inss_taxa = inss(salario)
  print("IRRF: R$ %s" % format_number(irrf(salario, inss_taxa)))
  sal_liquido = (salario - inss(salario)) - irrf(salario, inss_taxa)
  print("SALARIO LIQUIDO: R$ %s" % format_number(sal_liquido))


def buscar_funcionario(funcionarios):
  nome = input("Digite o nome do funcionario ")
  indice = 0
  for i, funcionario in enumerate(funcionarios):
    if (nome) in (funcionario):
      return funcionario 
      break

def inss(salario):
  if salario <= 1045:
    inss_taxa = (salario * 7.5)/100 # 1ª alíquota = 78.38
  if salario >= 1045.01 and salario <= 2089.60:
    des_taxa = (salario - 1045.01)*9/100 # 2ª alíquota = 94.01
    inss_taxa = des_taxa + 78.38
  if salario > 2089.61 and salario < 3134.40:
    des_taxa = (salario - 2089.61)*12/100 # 3ª alíquota
    inss_taxa = des_taxa + 172.39
  if salario > 3134.41 and salario < 6101.06:
    des_taxa = (salario - 3134.41)*14/100 # 4ª alíquota
    inss_taxa = des_taxa + 297.77
  if salario > 6101.06:
    inss_taxa = salario - 713,10 
  return inss_taxa

def irrf(salario, inss_taxa):
  base_irrf = salario - inss_taxa
  if base_irrf <= 1903.98:
    return 0
  if base_irrf >= 1903.99 and base_irrf  < 2826.65:
		 calculo_ir = (base_irrf * 7.5 )/ 100 - 142.80
  if base_irrf >= 2826.66 and base_irrf  < 3751.05: 
		 calculo_ir = (base_irrf * 15 )/ 100 - 354.8 
  if base_irrf >= 3751.06 and base_irrf  < 4664.68: 
		 calculo_ir = (base_irrf * 22.5 )/ 100 - 636.13 
  if base_irrf > 4664.69:
		 calculo_ir = (base_irrf * 27.5 )/ 100 - 869.63 

  return calculo_ir

def format_number(number, precision=2, group_sep='.', decimal_sep=','):
	"""
	Baseado em http://www.python.org.br/wiki/FormatarNumerosBrasil
	"""
	assert isinstance(number, float), 'Float esperado'
	assert isinstance(precision, int), 'Int esperado'
	assert isinstance(group_sep, str), 'Str esperado'
	assert isinstance(decimal_sep, str), 'Str esperado'

	number = '%.*f' % (max(0, precision), number)
	number = number.split('.')

	integer_part = number[0]

	if integer_part[0] == '-':
	    sign = integer_part[0]
	    integer_part = integer_part[1:]
	else:
	    sign = ''

	if len(number) == 2:
	    decimal_part = decimal_sep + number[1]
	else:
	    decimal_part = decimal_sep + '00'

	integer_part = list(integer_part)
	c = len(integer_part)

	while c > 3:
	    c -= 3
	    integer_part.insert(c, group_sep)

	return sign + ''.join(integer_part) + decimal_part

# PROGRAMA PRINCIPAL

def main():
  funcionarios = []

  while True:
    menu()
    op = int(input()) #Escolha da opcao
    if op == 1:
      cadastro_funcionario(funcionarios)
    if op == 2:
      contracheque(funcionarios)
    if op == 3:
      print("Programa encerrado")
      break

main()