# Exercise 13: Making Change - Kofei aparati mozg

print('''Կոֆեի ապառատը ընդունում է միայն 1000 դրամանոց թղթադրամ և 50, 100, 200 և 500 դրամանոց կոպեկներ։

1 - կապուչինո - 200 դրամ
2 - էսպրեսսո - 100 դրամ
3 - մակկոֆե - 150 դրամ
4 - նեսկաֆե - 100 դրամ
5 - թեյ լայմով - 100 դրամ
6 - թեյ դեղձով - 100 դրամ
7 - տաք շոկոլադ - 200 դրամ
8 - կաթով շոկոլադ - 250 դրամ
9 - դատարկ բաժակ - 50 դրամ
      ''')

choice = int(input('Ընտրել համապատասխան ըմպելիքը՝ '))
if choice not in range(1,10):
    print('Սխալ ընտրություն')
elif choice == 1 or choice == 7:
    choice = 200
elif choice == 2 or choice == 4 or choice == 5 or choice == 6:
    choice = 100 
elif choice == 3:
    choice = 150
elif choice == 8:
    choice = 250
else:
    choice = 50

print('Վճարեք', choice, 'դրամ')
print('''
Վճարման տարբերակներ՝
1 - 1000 դրամ
2 - 500 դրամ
3 - 200 + 100 դրամ
4 - 200 + 50 դրամ
5 - 200 դրամ
6 - 100 + 50 դրամ
7 - 100 դրամ
8 - 50 դրամ
''')
pox = int(input('Ընտրել վճարման տարբերակ՝ '))
if pox not in range(1,9):
    print('Սխալ ընտրություն')
    exit()
elif pox == 1:
    pox = 1000
elif pox == 2:
    pox = 500 
elif pox == 3:
    pox = 300
elif pox == 4:
    pox = 250
elif pox == 5:
    pox = 200
elif pox == 6:
    pox = 150
elif pox == 7:
    pox = 100
else:
    pox = 50

#manri veradardz
manr = pox - choice

hingharur = manr // 500
hingharurx = manr % 500
erkuharur = hingharurx // 200
erkuharurx = hingharurx % 200
harur = erkuharurx // 100
harurx = erkuharurx % 100
hisun = harurx // 50

if manr == 0:
    print('''
Դուք զդաչի չունեք, շնորհակալություն''')
    exit()
else:
    print('\nԶդաչին կազմում է՝', manr, 'դրամ')
    print('Տալիս ա մանր`')
    print(hingharur, 'հատ 500')
    print(erkuharur, 'հատ 200') 
    print(harur, 'հատ 100')
    print(hisun, 'հատ 50\n')
    print('Շնորհակալություն')