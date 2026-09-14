# calculadora soma 
n1= float(input("digite o primeiro número:"))
n2= float( input("digite o segundo número:"))

print ("o que voce deseja frazer com os números digitados?")
print ("1- somar")
print ("2- subtrair")   
print ("3- multiplicar")
opcao= int(input("digite a opção desejada:"))

if opcao == 1:
    resultado= n1+n2
    print (f"o resultado da soma é: {resultado}")
elif opcao == 2:
    resultado= n1-n2
    print (f"o resultado da subtração é: {resultado}")
elif opcao == 3:
    resultado= n1*n2
    print (f"o resultado da multiplicação é: {resultado}")
