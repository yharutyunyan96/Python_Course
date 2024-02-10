#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~EXERCISES 86~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~TAXI~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# print('''                                                               
#                                                                             WELCOME TO THE BEST TAXI SERVICE 
#                               /-----\\                                         IN Z WORLD  "Hopar Hopar"
#                              /  TAXI \\                         OUR DRIVER "GRNO DZYA" WILL TAKE YOU ANYWHERE LIKE SCHUMACHER
#                      _______/_________\\____________
#                     / _________     | _________     \\
#                    /  |        \    | |        \     \\
#                   /   |         \   | |         \     \\
#       ___________/    |__________\  | |__________\     \\______________
#      |                  _           |  _                    M5 BRABUS  |
#      |               MINIMAL        |      TAXI                        |
#      |               4 DOLLAR       |   HOPAR HOPAR                    | 
#    ]---|--------|----               |               |------|-------------[ 
#      \____OOO_______OOOO____________|_______________O0O_____OOOO /
#          OOOOO     OOOOOO                          OOOOO   OOOOOO
#           OOO       OOOO                            OOO     OOOO
                     
# ''') 
                
def taxi(kilometr):
    standart_gin = 4.00
    gin_metrov = 0.25
    metr = kilometr * 1000
    quantity = (metr / 140 )
    gin = round(standart_gin + (quantity * gin_metrov), 2)
    return gin

# heravorutyun = float(input(" Mutqagreq heravorutyuny kilometrov "))
# res = taxi(heravorutyun)
# print(f" Taxu giny: {res}$: QURS MANR CHUNEM!!!")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~EXERCISES 87~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ONLINE SHOPPING~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# def shopping(n):
#     if n == 1:
#         return 10.95
#     elif n > 1:
#         return 10.95 + (n - 1 ) * 2.95
#     else:
#         return 0.0
# n = int(input("Enter the quantity of shopping: "))
# if n < 0:
#     print("Wrong number")
# else:
#     price = shopping(n)
#     print(f"The price of shopping is {price}")