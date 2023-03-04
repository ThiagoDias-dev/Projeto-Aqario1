'''from time import sleep
print('\033[1:33m Olá, me chamo DORY e vou te ajudar a montar um aquário lindo e saudável\033[m') #Primeira área de interação, onde um atendente virtual se apresenta ao usuário
sleep(1)
print('\033[1mVamos coletar algumas informações...\033[m \n') #Mais uma interação com o úsuário infoando que ele deverá fornecer algumas informações
sleep(1)'''

medida1 = int(input('\033[4mQual a largura do seu aquário:  '))#Usuário informa as medidas do aquário
medida2 = int(input('033mQual a profundidade do seu aquário:  '))
medida3 = int(input('Qual a altura do seu aquário:  \033[m'))

litragem = (medida3 * medida2 * medida1) / 1000
print('Seu aquário tem \033[1:31m{}\033[m litros'.format(litragem)) #Resposta do resultado das medidas do aquário do usuário
for c in range(1):
        DOCE = 0
        SALGADO = 0
        usuario = 0

        tipoaquario = str(input('\n QUAL O TIPO DO SEU AQUÁRIO? \033[1:34m[SALGADO/DOCE]\033[m')).upper().strip()
while usuario != 4:
        if tipoaquario == 'SALGADO':
         usuario = int(input('Escolha uma das opções abaixo para saber mais...\n'
        '[1] Condicionador PRIME\n'
        '[2]Ativado Biológico STABILITY\n'
        '[3]PH ideal para o seu aquário\n'
        '[4]FIM DO PROGRAMA: \n >>>  '))
        prime = 1
        stability = 2
        ph = 3
        if usuario == 1:
                doseprime = litragem // 2
                print('Você vai precisar adcionar {:.0f} gotas de prime à água do seu aquário'.format(doseprime))
        elif usuario == 2:
                dosestability = litragem // 8
                dosestability2 = dosestability // 2
                print('Você vai precisar de {:.0f}ml de STABILITY no primeiro dia...'.format(dosestability))
                print('e {:.0f}ml de STABILITY nos 8 dias seguintes!'.format(dosestability2))
        elif usuario == 3:
                print('O PH ideal para aquário marinho é entre 7.8 e 8.4 e a temperatura de aproximadamente 26ºC')
        elif usuario == 4:
                print('FIM DO PROGRAMA, VOLTE SEMPRE QUE PRECISAR')

        if tipoaquario == 'DOCE':
                usuario1 = int(input('Escolha uma das opções abaixo para saber mais...\n'
                '[1] Condicionador PRIME\n'
                '[2]Ativado Biológico STABILITY\n'
                '[3]PH ideal para o seu aquário\n'
                '[4]FIM DO PROGRAMA: \n >>>  '))
                prime = 1
                stability = 2
                ph = 3
        if usuario1 == 1:
                doseprime = litragem // 2
                print('Você vai precisar adcionar {:.0f} gotas de prime à água do seu aquário'.format(doseprime))
        elif usuario1 == 2:
                        dosestability = litragem // 8
                        dosestability2 = dosestability // 2
                        print('Você vai precisar de {:.0f}ml de STABILITY no primeiro dia...'.format(dosestability))
                        print('e {:.0f}ml de STABILITY nos 8 dias seguintes!'.format(dosestability2))
        elif usuario1 == 3:
                        print('Aquário de água doce respeitam 3 faixas de PH: '
                              '6.2 a 6.8: Quer dizer se seu PH está ÁCIDO'
                              '6.8 a 7.2: Quer dizer que seu PH está NEUTRO'
                              '7.2 a 7.6: Quer dizer que seu PH está ALCALINO')
        elif usuario == 4:
                        print('FIM DO PROGRAMA, VOLTE SEMPRE QUE PRECISAR')









