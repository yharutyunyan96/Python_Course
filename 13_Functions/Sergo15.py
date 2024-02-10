#~~~~EXERCISES 106~~~~ days in month
# def amsativ(amis , tari):
#     if amis < 1 and amis > 12 or len(str(tari)) != 4:
#         return "Tikin duq sxalveleq"
#
#     amsativ = [31,28,31,30,31,30,31,31,30,31,30,31]
#
#     if (tari % 4 == 0 and tari % 100 != 0 ) or (tari % 400 == 0):
#         amsativ[1] = 29
#         print("Nahanj tari")
#         return amsativ[amis+1]
#     else:
#         print("Sovorakan tari")
    
# amis = int(input("Enter the month from 1 to 12: "))
# tari = int(input("Enter the year: "))
#
# result = amsativ(amis, tari)
# if type(result) == int:
#     print(f"Month {amis} , Year {tari} : Quantity days in month {result}")
# else:
#     print(result)  # ~~~~vonc amsva orery tpenq

#~~~~EXERCISES 109 magic date

# def fantastik_taretiv(day, amis , tari):
#     if day < 1 or amis < 1 or amis > 12 or len(str(tari)) != 4:
#         return "Tikin duq sxalveleq"

#     magic = day * amis

#     verjin_tvanshanner = tari % 100

#     return magic == verjin_tvanshanner

# print("20-rd dari fantastik taretvery")

# for tari in range(1900,2000):
#     for amis in range(1,13):
#         for day in range(1,32):
#             if fantastik_taretiv( day ,amis , tari ):
#                 print(f"{day} , {amis} , {tari} \n" )