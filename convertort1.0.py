# Funções que irão converter as temperaturas
from controller.funcoes import celsius_para_kelvin, celsius_para_fahrenheit, kelvin_para_celsius, kelvin_para_fahrenheit, fahrenheit_para_celsius, fahrenheit_para_kelvin

from model.historico import historico

# Curiosidades para ajudar os usuários do programa:
curiosidades = (
    'Curiosidades:\n'
    'Ponto de fusão (congelamento) da água nas seguintes temperaturas, são:\n'
    'Celsius (ºC) = 0ºC\n'
    'Kelvin (ºK) = 273.15ºK\n'
    'Fahrenheit (ºF) = 32ºF\n'
)
print(curiosidades)

# Looping usando While
while True:
    # Menu
    print('=' * 100)
    menu = (
        '\nConversor de temperaturas Celsius (ºC), Kelvin (ºK) e Fahrenheit (ºF):\n'
        'Para converter de Celsius para Kelvin, digite 1\n'
        'Para converter de Celsius para Fahrenheit, digite 2\n'
        'Para converter de Kelvin para Celsius, digite 3\n'
        'Para converter de Kelvin para Fahrenheit, digite 4\n'
        'Para converter de Fahrenheit para Celsius, digite 5\n'
        'Para converter de Fahrenheit para Kelvin, digite 6\n'
        'Ver histórico, digite 0\n'
    )
    print(menu)

    convertor = float(input('Digite o número que relaciona à temperatura que deseja converter: '))
    print(convertor)

    if convertor == 1:
        celsius = float(input('Digite a temperatura em Celsius para converter para Kelvin: '))
        print(f'O resultado da conversão foi: {celsius_para_kelvin(celsius):.2f}ºK')
        historico['Celsius para Kelvin'] += 1

    elif convertor == 2:
        celsius = float(input('Digite a temperatura em Celsius para converter para Fahrenheit: '))
        print(f'O resultado da conversão foi: {celsius_para_fahrenheit(celsius):.2f}ºF')
        historico['Celsius para Fahrenheit'] += 1

    elif convertor == 3:
        kelvin = float(input('Digite a temperatura em Kelvin para converter para Celsius: '))
        print(f'O resultado da conversão foi: {kelvin_para_celsius(kelvin):.2f}ºC')
        historico['Kelvin para Celsius'] += 1

    elif convertor == 4:
        kelvin = float(input('Digite a temperatura em Kelvin para converter para Fahrenheit: '))
        print(f'O resultado da conversão foi: {kelvin_para_fahrenheit(kelvin):.2f}ºF')
        historico['Kelvin para Fahrenheit'] += 1

    elif convertor == 5:
        fahrenheit = float(input('Digite a temperatura em Fahrenheit para converter para Celsius: '))
        print(f'O resultado da conversão foi: {fahrenheit_para_celsius(fahrenheit):.2f}ºC')
        historico['Fahrenheit para Celsius'] += 1

    elif convertor == 6:
        fahrenheit = float(input('Digite a temperatura em Fahrenheit para converter para Kelvin: '))
        print(f'O resultado da conversão foi: {fahrenheit_para_kelvin(fahrenheit):.2f}ºK')
        historico['Fahrenheit para Kelvin'] += 1

    # Condicional que imprime o histórico de conversões
    elif convertor == 0:
        print("\nHistórico de conversões:")
        for conversao, quantidade in historico.items():
            print(f"{conversao}: {quantidade} vez(es)")

    # Condicional que alerta sobre uma opção inválida, que
    # não está sendo mostrada no menu
    else:
        print('\nOpção inválida!\n')

    # Variável que faz o controle de parada do looping
    continuar = input('\nDeseja fazer a conversão de mais uma temperatura? (s/n) \n')
    if continuar.lower() != 's':
        break

print('\nPrograma encerrado!\n')
