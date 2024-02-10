# EXERCISES 35 --- IS THE NUMBER ENTERED EVEN?

# print( " Enter the number and i will tell you the number is even or odd \n" )

# number1 = int(input( " Please enter the number: " ))

# if number1 % 2 == 0:
#     print( " The number is even " )

# else:
#      print( " The number is odd " )

# EXERCISES 36 Dog's year's

# shan_tariq = float(input( " Enter the dog's age: " ))

# if shan_tariq <= 0:
#     print ( " Please enter the correct age " )

# if shan_tariq > 0 and shan_tariq <= 2:
#     print( "Dog's year in human's life is " , shan_tariq * 10.5 )

# if shan_tariq > 2:
#     shan_tariq = (shan_tariq - 2) * 4 + 21
# print( "Dog's year in human's life is " , shan_tariq ) ?????????????????

# EXERCISES 37 WHAT IS FIGURE

# print( "                                                          Attention please this is important " )

# print( "                                           The drawings are the ideas of Yuri Harutyunyan and they are licensed " )

# print (" Enter the number of angles and i will tell you what is figure ")

# angle = int(input( " Please enter the number of angles from 3 to 10: " ))

# if 3 > angle > 10:

#     print( " Incorrect number of angles entered " ) 

# elif angle == 3:

#     print( ''' The figure is Triangle    
          
# |\ 
# |  \ 
# |    \ 
# |      \ 
# |        \ 
# |          \ 
# |            \ 
# |              \ 
# |________________\ 
          

# ''' )
    
# elif angle == 4:
#     print( ''' This is a square figure

# ----------------------------------------
# |                                      |
# |                                      |
# |                                      |
# |                                      |
# |                                      | 
# |                                      |
# |                                      |
# ---------------------------------------- 
#           ''')  

# elif angle == 5:
#     print('''This is a pentagon figure
          
#          ---------------
#         /               \ 
#        /                 \ 
#       /                   \ 
#      /                     \ 
#      \                     /
#       \                   /
#        \                 /
#         \               /
#          ---------------    
#           ''')         

# elif angle == 6:
#     print( ''' This is a hexagon figure
          
#          /\ 
#         /  \ 
#        /    \ 
#       /      \ 
#      /        \ 
#     |          |
#     |          |
#     |          | 
#     |          |
#     |          |
#      \        /
#       \      /
#        \    /
#         \  /  
#          \/
          
#           ''')   
    
# elif angle == 7:
#     print(''' This is a heptagon figure
          
#                  ---------------
#                 /               \ 
#                /                 \ 
#               /                   \                                                                        
#              |                     |
#              |                     |
#              |                     |
#              |                     |
#              \                     /
#               \                   /
#                \                 /
#                 \               /
#                   \            /
#                    \          / 
#                     \        /
#                      \      /
#                       \    /
#                        \  /
#                         \/


#           ''') 
    
# elif angle == 8:
#     print(''' 
          
#                                                    /\ 
#                                                   /  \ 
#                                                  /    \ 
#                                                 /      \  /\ 
#                                                /        \/  \ 
#                                                \        /    \ 
#                                                 \      /      \ 
#                                                  \    /\      /
#                                                   \  /  \    /
#                                                    \/    \  /
#                                                           \/
#           ''')
    
# elif angle == 9:
#     print('''
#                                                    /\        /\ 
#                                                   /  \      /  \ 
#                                                  /    \    /    \ 
#                                                 /      \  /      \ 
#                                                /        \/        \ 
#                                                \                  /
#                                                 \                /----------
#                                                  \    /\                    \ 
#                                                   \  /  \                    \ 
#                                                    \/    \              /\     \ 
#                                                           \            /  \    / 
#                                                            \          /    \  /
#                                                             \        /      \/
#                                                              \      /
#                                                               \    /
#                                                                \  / 
#                                                                 \/

#           ''')
# else:
#     print ( " You wrote the wrong number of angles " )