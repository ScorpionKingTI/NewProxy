import os, requests, time
def gt():
   print('\n\033[34;01mdeseja gerar mas proxys?\n1. sim\n2. sair\n\033[0;0m\n')
   df=input('>')
   if df == '1':
    mn()
   elif df == '2':
    print('\n\033[32;1mobrigado por usar os serviços do scorpion king\033[0;0m\n')
    exit()
   elif df != 1 and 2:
    print('\n\033[33;1mseleção invalida digite 1 ou 2\n')
    gt()
os.system('clear')
print("                    coded by:")
time.sleep(0.1)      
print("")
time.sleep(0.1)      
print("       ⟡ ━━━━━━━━ ⟡ ━━━━━━━━ ⟡ ━━━━━━━━ ⟡ ")
time.sleep(0.1)      
print("       ┃                                ┃")
time.sleep(0.1)       
print("       ┃      ✪   SCORPION KING   ✪    ┃")
time.sleep(0.1)      
print("       ┃                                ┃")
time.sleep(0.1)      
print("       ⟡ ━━━━━━━━ ⟡ ━━━━━━━━ ⟡ ━━━━━━━━ ⟡")  
print('')
time.sleep(5)
def mn():
 print('''\033[34;1m
 _____________________________________________
 |   country (pais)   |   initials (sigla)   |
 +--------------------+----------------------|    
 |     AFEGANISTÃO    |          af          |
 |      ARGENTINA     |          ar          |
 |      AUSTRÁLIA     |          au          |
 |       BÉLGICA      |          be          |
 |       BOLIVIA      |          bo          |
 |       BRAZIL       |          br          |
 |       CANADA       |          ca          |
 |       SUIÇA        |          ch          |
 |       CHILE        |          cl          |                                
 |      COLÔMBIA      |          co          |
 |      ALEMANHA      |          de          |
 |     DINA MARCA     |          dk          |
 |       EGITO        |          eg          |
 |      ESPANHA       |          es          |
 |      FRANÇA        |          fr          |
 |    REINO UNIDO     |          gb          |
 |     HONG-KONG      |          hk          |
 |     INDONÉSIA      |          id          |
 |       INDIA        |          in          |
 |      ITALIA        |          it          |
 |      JAMAICA       |          jm          |
 |       JAPÃO        |          jp          |
 |      PORTUGAL      |          pt          |
 |      TURQUIA       |          tr          |
 |   ESTADOS UNIDOS   |          us          |
 |      RUSSIA        |          rus         |
 |      randon        |          all         |
 +--------------------+----------------------+
 Esta tabela mostra paises mas comuns mas junto a esta ferramenta esta um arquivo pdf com todos os paises e siglas
 ''')
 t=input('\nDigite a sigla do pais que deseja obter proxys\n> ')
 s=requests.get('https://api.proxyscrape.com?request=displayproxies&proxytype=https&timeout=7000&country={}&anonymity=elite&ssl=no&limit=50&formato=json'.format(t)).text
 print('\033[34;1m\n◆-▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱-◆\n◆-\n\n',s,'\n◆-\n◆-▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱-◆\n')
 gt()
mn()
