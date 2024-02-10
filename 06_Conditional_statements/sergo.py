print ('''
       
8     |||     |||     |||     |||         This is a chess board, 
                                          enter the coordinates of the square.
7 |||     |||     |||     |||             and I will tell you, the square is black or white.
                        
6     |||     |||     |||     |||
                     
5 |||     |||     |||     |||    
                  
4     |||     |||     |||     |||
                  
3 |||     |||     |||     |||    
                
2     |||     |||     |||     |||
                   
1 |||     |||     |||     |||    
       
   a   b   c   d   e   f   g   h
''')
a = "_abcdefgh"

coord = input(" Enter the coordinate: ")
if coord[0] in a and coord[1].isdigit():
    tar = coord [0]

    horizontally_coord = a.find (tar)

    verticaly_coord = int(coord [1])

    if ( horizontally_coord + verticaly_coord ) % 2 == 0:
        print( " The square is black " )

    else:print( "The square is white " )
else:
    print('please valid coordinates.')