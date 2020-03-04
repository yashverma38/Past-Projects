"""making a matrix for tic-tac-toe where every blocK is given a number and making a matrix of it"""
M = [[11, 12, 13], [21, 22, 23], [31, 32, 33]]
##Printing the elemts of list in matrix liKe order
for elems in M:
    print(elems)
##Infinite loop which doesn't break until the game is over
N = 0
##It is a system that worKs for both players for odd/even number
while N >= -1:
##For even number player 1 plays
    if (N%2+1) == 1:
        A = input(f'Player {(N%2)+1} move:')
##The input is taKen in the form of number string,  e.g 11,33(ColRow)
        N += 1
        if A == "":
            print("No move is wrong move")
            N = N-1
            for elems in M:
                print(elems)
##Every move is printed in the same matrix
            continue
        if M[int(A[0])-1][int(A[1])-1] == -2:
##Checking if the move is already done by other player
            print("Wrong Move ")
            N = N-1
            for elems in M:
                print(elems)
            continue
##Continue so that the process is sKipped and it player 1 plays again
        if M[int(A[0])-1][int(A[1])-1] == -1:
            print("Alredy done")
##Checking if the move is already played by our player
            N = N-1
            for elems in M:
                print(elems)
            continue
        M[int(A[0])-1][int(A[1])-1] = -1
##Making the move
        for elems in M:
            print(elems)
        K1 = (M[0][0] == M[0][1] == M[0][2])
        K2 = (M[1][0] == M[1][1] == M[1][2])
        K3 = (M[2][0] == M[2][1] == M[2][2])
        K4 = (M[0][0] == M[1][0] == M[2][0])
        K5 = (M[0][1] == M[1][1] == M[2][1])
        K6 = (M[0][2] == M[1][2] == M[2][2])
        K7 = (M[0][0] == M[1][1] == M[2][2])
        K8 = (M[0][2] == M[1][1] == M[2][0])
        TRUTH = [K1, K2, K3, K4, K5, K6, K7, K8]
        if any(TRUTH):
            print("Player 1 Wins")
            break
        K = 1
        for rum in M:
            for num in rum:
                K = K*num
        if K in (-16, -32):
            print("We never Wanted it, but it is a TIE")
            break
##Realising ties##
    if (N%2+1) == 2:
        B = input(f'Player {(N%2)+1} move:')
        N += 1
        if B == "":
            print("No move is wrong move")
            N = N-1
            for elems in M:
                print(elems)
            continue
        if M[int(B[0])-1][int(B[1])-1] == -1:
            print("Wrong Move")
            N = N-1
            for elems in M:
                print(elems)
            continue
        if M[int(B[0])-1][int(B[1])-1] == -2:
            print("Alredy done")
            N = N-1
            for elems in M:
                print(elems)
            continue
        M[int(B[0])-1][int(B[1])-1] = -2
        for elems in M:
            print(elems)
        K1 = (M[0][0] == M[0][1] == M[0][2])
        K2 = (M[1][0] == M[1][1] == M[1][2])
        K3 = (M[2][0] == M[2][1] == M[2][2])
        K4 = (M[0][0] == M[1][0] == M[2][0])
        K5 = (M[0][1] == M[1][1] == M[2][1])
        K6 = (M[0][2] == M[1][2] == M[2][2])
        K7 = (M[0][0] == M[1][1] == M[2][2])
        K8 = (M[0][2] == M[1][1] == M[2][0])
        TRUTH = [K1, K2, K3, K4, K5, K6, K7, K8]
        if any(TRUTH):
            print("Player 2 Wins")
            break
        K = 1
        for rum in M:
            for num in rum:
                K = K*num
        if K in (-16, -32):
            print("We never Wanted it, but it is a TIE")
            break
            
