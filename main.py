import random


# board = [
#     [7,8,0,4,0,0,1,2,0],
#     [6,0,0,0,7,5,0,0,9],
#     [0,0,0,6,0,1,0,7,8],
#     [0,0,7,0,4,0,2,6,0],
#     [0,0,1,0,5,0,9,3,0],
#     [9,0,4,0,6,0,0,0,5],
#     [0,7,0,3,0,0,0,1,2],
#     [1,2,0,0,0,7,4,0,0],
#     [0,4,9,2,0,6,0,0,7]
# ]
newBo = [[0 for x in range(9)] for y in range(9)]
board = [[0 for x in range(9)] for y in range(9)]


# def initializeBoard(bo):
#     counter=0
#
#     for i in range(9):
#         for j in range(9):
#
#             num = random.randint(0, 9)
#             print( num)
#
#             if num == 0:
#                 bo[i][j] = num
#                 counter=counter+1
#             else:
#                 if valid(board1,num,[i,j]):
#                     bo[i][j] = num
#                 else:
#                     num = random.randint(0, 9)
#                     while True:
#                         if valid(board1,num,[i,j]):
#                             bo[i][j] = num
#                             break
#                         else:
#                             num =random.randint(0, 9)
#
#     print(",,,,,"+(str)(board1[0][0]))
#
#
#
# def inRowCol(num,row,col):
#     for i in range(9):
#         if board1[row][i] == num and col != i:
#             return True
#         for i in range(9):
#             if board1[i][col] == num and row != i:
#                 return True
#
#     return False
def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find
    listNum=[1,2,3,4,5,6,7,8,9]
    random.shuffle(listNum)

    for i in listNum:
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False
# def solve(bo):
#     find = find_empty(bo)
#     if not find:
#         return True
#     else:
#         row, col = find
#
#     for i in range(1,10):
#         if valid(bo, i, (row, col)):
#             bo[row][col] = i
#
#             if solve(bo):
#                 return True
#
#             bo[row][col] = 0
#
#     return False


def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True


def print_board(bo):
    print("in printing the board")
    for i in range(len(bo)):
        if i % 3 == 0 :
            print("----------------------------------")

        for j in range(len(bo[0])):
            if j % 3 == 0 :
                print("| ", end="")

            if j == 8:
                if bo[i][j] == 0 or bo[i][j] ==" " or bo[i][j] != board[i][j]:
                    print(" "+str(bo[i][j]) + " ", "|")
                else:
                    print("."+str(bo[i][j]) + " ", "|")
            else:
                if bo[i][j] == 0  or bo[i][j] ==" " or bo[i][j] != board[i][j]:
                    print(" "+str(bo[i][j]) + " ", end="")
                else:
                    print( "."+str(bo[i][j]) + " ", end="")


        if i == 8:
            print("----------------------------------")


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col

    return None


def deleteCells(bo,spacedCell,pos):

    num = random.randint(0, 8)
    num2 = random.randint(0, 8)
    if spacedCell == 0:
        return
    if pos == (num, num2):
        return deleteCells(bo,spacedCell,pos)
    if pos != (num , num2):
        bo[num][num2] =0
        return deleteCells(bo,spacedCell-1,(num,num2))

def getNewBoard(bo):
    for i in range(9):
        for j in range(9):
            newBo[i][j] = bo[i][j]

def addOnNewBoard(num,pos):

    #find=find_empty(newBo)
    print(pos)
    row , col = pos

    if board[row][col] != 0:
        print("invalide position")
    else:
        if valid(newBo, num, (row, col)):
            newBo[row][col] = num
            print_board(newBo)
        else:
            print("invalide inpute")

def checkSolved(bo):

    for i in range(9):
        for j in range(9):
           if not valid(bo, newBo[i][j], (i,j)):
               return False

    return True



#
#


# print_board(board1)
# solve(board1)
# print_board(board1)

def main():
    #print_board(board)
    solve(board)
    #print("___________________")
    #print_board(board)
    #print(checkSolved(board))
    print("************************************")
    print("how many empty cells you want ?")
    inp = input()
    deleteCells(board, int(inp), (0, 0))
    print_board(board)
    getNewBoard(board)
    print_board(newBo)
    print(checkSolved(board))
    addOnNewBoard(8, (0, 1))
    while True:
        if checkSolved(newBo):
            print("the board is solved")
            break
        else:
            print("ener the number in format: z x y")
            inp = input()
            xyz = inp.split()
            xyz = [int(i) for i in xyz]
            addOnNewBoard(xyz[0], (xyz[1], xyz[2]))


if __name__ == '__main__':main()

