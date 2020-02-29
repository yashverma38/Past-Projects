## Making a matrix for the tic-tac-toe where every block is given a number and making a matrix of it
m = [[11,12,13],[21,22,23],[31,32,33]]
##Printing the elemts of list in matrix like order
for elems in m:
    print (elems)
##Infinite loop which doesn't break until the game is over
n=0

##It is a system that works for both players for odd/even number

while n>=-1:
##For even number player 1 plays
    if (n%2+1) == 1:
        a = input(f'Player {(n%2)+1} move:' )
##The input is taken in the form of number string,  e.g 11,33(ColRow)
        n+=1
        if a == "": 
            print("No move is wrong move")
            n = n-1
            for elems in m:
                print (elems)
##Every move is printed in the same matrix
            continue
        if m[int(a[0])-1][int(a[1])-1] == -2: 
##Checking if the move is already done by other player
            print("Wrong Move ")
            n = n-1
            for elems in m:
                print (elems)
            continue
##Continue so that the process is skipped and it player 1 plays again
        if m[int(a[0])-1][int(a[1])-1] == -1:
            print("Alredy done")
##Checking if the move is already played by our player
            n = n-1
            for elems in m:
                print (elems)
            continue
        m[int(a[0])-1][int(a[1])-1] = -1
##Making the move
        for elems in m:
             print (elems)
        if m[0][0] == m[0][1] == m[0][2] or m[1][0] == m[1][1] == m[1][2] or m[2][0] == m[2][1] == m[2][2] or m[0][0]==m[1][0]==m[2][0] or m[0][1]==m[1][1]==m[2][1] or m[0][2]==m[1][2]==m[2][2] or m[0][0]==m[1][1]==m[2][2] or m[0][2]==m[1][1]==m[2][0]:
            print ("Player 1 Wins")
            break
        k = 1
        for rum in m:
            for num in rum:
                k = k*num
        if k ==-16 or k== -32:
            print("We never Wanted it, but it is a TIE")
            break
##Realising ties
    if (n%2+1) == 2:
        
        b = input(f'Player {(n%2)+1} move:' )
        n+=1
        if b == "": 
            print("No move is wrong move")
            n = n-1
            for elems in m:
                print (elems)
            continue
        if m[int(b[0])-1][int(b[1])-1] == -1:
            print("Wrong Move")
            n=n-1
            for elems in m:
                print (elems)
            continue
        if m[int(b[0])-1][int(b[1])-1] == -2:
            print("Alredy done")
            n = n-1
            for elems in m:
                print (elems)
            continue
        m[int(b[0])-1][int(b[1])-1] = -2
        for elems in m:
            print (elems)
        if m[0][0] == m[0][1] == m[0][2] or m[1][0] == m[1][1] == m[1][2] or m[2][0] == m[2][1] == m[2][2] or m[0][0]==m[1][0]==m[2][0] or m[0][1]==m[1][1]==m[2][1] or m[0][2]==m[1][2]==m[2][2] or m[0][0]==m[1][1]==m[2][2] or m[0][2]==m[1][1]==m[2][0]:
            print ("Player 2 Wins")
            break
        k = 1
        for rum in m:
            for num in rum:
                k = k*num
        if k ==-16 or k== -32:
            print("We never Wanted it, but it is a TIE")
            break
            