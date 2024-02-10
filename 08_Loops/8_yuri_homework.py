# Exercise 56: Frequency to Name
# r_list = [
#   'Radio Waves',          #Less than 3 × 10**9
#   'Microwaves',           #3 × 10**9 to less than 3 × 10**12
#   'Infrared Light',       #3 × 10**12 to less than 4.3 × 10**14
#   'Visible Light',        #4.3 × 10**14 to less than 7.5 × 10**14
#   'Ultraviolet Light',    #7.5 × 10**14 to less than 3 × 10**17
#   'X-Rays',               #3 × 10**17 to less than 3 × 10**19
#   'Gamma Rays'            #3 × 10**19 or more
# ]

# user_input = int(input('Enter frequency of some radiation in HZ'))

# freq_list = [
#   [user_input < 3 * 10**9],
#   [3 * 10**9 <= user_input < 3 * 10**12],
#   [3 * 10**12 <= user_input < 4.3 * 10**14],
#   [4.3 * 10**14 <= user_input < 7.5 * 10**14],
#   [7.5 * 10**14 <= user_input < 3 * 10**17],
#   [3 * 10**17 <= user_input < 3 * 10**19],
#   [user_input >= 3 * 10**19],
# ]

# for i in range(len(r_list)):
#   if freq_list[i]:
#     print(r_list[i])
#     break



#mnacac@ heto kanem



"""                    
       ( -O-   -O- )      ------------------
             |             LooooP EXERCICES
           =====          ------------------             
"""                                

# Exercise 63: Average
# x = []
# while True:
#   x.append(input("enter something: "))
#   if x[-1] != '0':
#     print(x)
#     continue
#   elif x[0] == '0':
#     print('First item cennot be zero!')
#   else:
#     #gtnum enq mijin@
#     avg = (len(x)-1)/2
#     print(f"Average number of entered items is {avg}.")
#   break


# Exercise 64: Discount Table
new_pricelist = []
old_pricelist = []
while True:
  x = float(input("Enter old price (to stop press 0): "))
  new_pricelist.append(x)
  # old_pricelist.append(x)

  if new_pricelist[-1] != 0:
    y = round(x * 2.5, 2)    #60 tokos zexch@ het hashvark@ 2.5 a anum
    old_pricelist.append(y)
    continue
  elif new_pricelist[0] == 0:
    print('First item cennot be zero!')
  else:
    #0i depqum STOP a anum print enq anum aranc 0-i lister@ [:-1]
    print(f'New price - {new_pricelist[:-1]} BLACK FRIDAY! -60%')
    print(f'Old price - {old_pricelist}')
  break
