# desafio-python

O desafio consiste em desenvolver um sistema para controle de folha de pagamento de 
uma empresa, conforme os detalhes abaixo.

Para salários acima de R$6.101,06, o desconto é fixado em R$713,10. 
Vamos fazer um exemplo de cálculo de desconto do INSS considerando um salário de 
R$5000,00:

‒ 1ª alíquota: R$1045,00 * 7,5% = R$78,38
‒ 2ª alíquota: (R$2089,60 – R$1045,01) * 9% = R$94,01
‒ 3ª alíquota: (R$3134,40 – R$2089,61) * 12% = R$125,38‒ 4ª alíquota: (R$5000,00 – R$3134,41) * 14% = R$261,18
‒ Desconto INSS = R$78,38 + R$94,01 + R$125,38 + R$261,18 = R$558,95

O cálculo do desconto do IRRF segue a tabela da imagem abaixo. O valor utilizado para 
cálculo deve ser o valor do salário bruto menos o valor do desconto de INSS. Para o IRRF,
o cálculo é mais simples que no INSS, pois ele não é feito de forma progressiva. Basta 
verificar em qual faixa o valor se encaixa, descontar a percentual alíquota e depois a parcela 
dedutível.
