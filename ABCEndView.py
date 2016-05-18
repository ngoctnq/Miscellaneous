#!/usr/bin/env python

from copy import deepcopy
from timeit import default_timer
from Tkinter import *
import tkMessageBox

# params: rows/columns, count, head/tail

# problem 209
#constraint = [[['A',''],['C','D'],['A',''],['','C'],['E',''],['','E'],['E','']],
#                [['A',''],['','A'],['B',''],['','B'],['','B'],['C','D'],['B','']]]
#choices = 'ABCDE'

# problem 3
# constraint = [[['',''],['',''],['A','']],[['','B'],['',''],['','']]]
# choices = 'AB'

# problem 176
constraint = [[['A',''],['','A'],['D',''],['',''],['','E'],['',''],],
                [['','E'],['','B'],['E',''],['','D'],['C',''],['','C']]]
choices = 'ABCDE'

# last problem of the month
#constraint = [[['',''], ['B',''], ['A',''], ['B',''], ['D','B'], ['B','A'], ['',''], ['','']],
#              [['D','B'], ['C','D'], ['','B'], ['C','D'], ['',''], ['C','B'], ['',''], ['','D']]]
#choices = 'ABCD'

dim = len(constraint[0])
diag = True





# GUI PART
not_entered = True
while not_entered:
    text = raw_input("Dimension (n x n)? ")

    try:
        dim = int(text)
        not_entered = False
        if dim < 2:
            raise ValueError
    except ValueError:
        print "Value error!", "Dimension has to be an integer greater than 1!"

constraint = [[],[]]
for i in range(dim):
    constraint[0].append(['',''])
    constraint[1].append(['',''])
#______________

def not_cap_chars(word):
    for i in range(len(word)):
        if ord(word[i]) != ord('A')+i:
            return True
    return False

not_entered = True
while not_entered:
    choices = raw_input("Characters to fill in, with no delimiters: ").upper()
    if not_cap_chars(choices):
        print "String error!", "Only sequencial capital letters are allowed."
    elif len(choices) >= dim:
        print "String error!", "Number of choices must be less than "+str(dim)+"."
    else:
        not_entered = False
#______________

not_entered = True
while not_entered:
    constraint_sub = raw_input("Insert row-beginning constraints - Continuously, '-' for none: ").upper()
    if len(constraint_sub) != dim:
        print "Constraints error!", "Number of constraints must be exactly "+str(dim)+"."
    else:
        legit = True
        while legit:
            for i in range(dim):
                if constraint_sub[i] in choices:
                    constraint[0][i][0] = constraint_sub[i]
                elif constraint_sub[i] != '-':
                    legit = False
                    print "String error!", constraint_sub[i]+" is not a valid entry!"
                    break
            if i == dim-1:
                break
        if legit:
            not_entered = False
#______________

not_entered = True
while not_entered:
    constraint_sub = raw_input("Insert row-ending constraints - Continuously, '-' for none: ").upper()
    if len(constraint_sub) != dim:
        print "Constraints error!", "Number of constraints must be exactly "+str(dim)+"."
    else:
        legit = True
        while legit:
            for i in range(dim):
                if constraint_sub[i] in choices:
                    constraint[0][i][1] = constraint_sub[i]
                elif constraint_sub[i] != '-':
                    legit = False
                    print "String error!", constraint_sub[i]+" is not a valid entry!"
                    break
            if i == dim-1:
                break
        if legit:
            not_entered = False
#______________

not_entered = True
while not_entered:
    constraint_sub = raw_input("Insert column-beginning constraints - Continuously, '-' for none: ").upper()
    if len(constraint_sub) != dim:
        print "Constraints error!", "Number of constraints must be exactly "+str(dim)+"."
    else:
        legit = True
        while legit:
            for i in range(dim):
                if constraint_sub[i] in choices:
                    constraint[1][i][0] = constraint_sub[i]
                elif constraint_sub[i] != '-':
                    legit = False
                    print "String error!", constraint_sub[i]+" is not a valid entry!"
                    break
            if i == dim-1:
                break
        if legit:
            not_entered = False
#______________

not_entered = True
while not_entered:
    constraint_sub = raw_input("Insert column-ending constraints - Continuously, '-' for none: ").upper()
    if len(constraint_sub) != dim:
        print "Constraints error!", "Number of constraints must be exactly "+str(dim)+"."
    else:
        legit = True
        while legit:
            for i in range(dim):
                if constraint_sub[i] in choices:
                    constraint[1][i][1] = constraint_sub[i]
                elif constraint_sub[i] != '-':
                    legit = False
                    print "String error!", constraint_sub[i]+" is not a valid entry!"
                    break
            if i == dim-1:
                break
        if legit:
            not_entered = False
#______________
            
root = Tk()
root.withdraw()
result = tkMessageBox.askquestion("ABC End View Solver", "Are diagonals required to have all characters?")
if result == 'yes':
    diag = True
else:
    diag = False
#______________




# start reinitializing
choices += 'X'
maxX = dim-len(choices)+1
trials_count = 0
solutions_count = 0

def reset_board(board):
    for i in range(dim):
        for j in range(dim):
            board[i][j] = 'X'

def min_coord(board):
    curr = None
    currMin = 10 # arbitrary large number
    for i in range(dim):
        for j in range(dim):
            currLen = len(board[i][j])
            if currLen == 2:
                return [i,j]
            if currLen < currMin and currLen > 1:
                currMin = currLen
                curr = [i,j]
    return curr

def is_deadend(board):
    for i in range(dim):
        for j in range(dim):
            if len(board[i][j]) > 1:
                return False
    return True

def has_no_null(board):
    for i in range(dim):
        for j in range(dim):
            if len(board[i][j]) == 0:
                return False
    return True

def is_legit(board):
    # check rows
    for i in range(dim):
        temp = ''
        count = 0
        for j in range(dim):
            if board[i][j] == 'X':
                count += 1
            temp += board[i][j]
        if count > maxX:
            return False
        for j in choices:
            if j not in temp:
                return False
    # check columns
    for i in range(dim):
        temp = ''
        count = 0
        for j in range(dim):
            if board[j][i] == 'X':
                count += 1
            temp += board[j][i]
        if count > maxX:
            return False
        for j in choices:
            if j not in temp:
                return False   

    # check diagonals
    if diag:
        temp = ''
        count = 0
        for j in range(dim):
            if board[j][j] == 'X':
                count += 1
            temp += board[j][j]
        if count > maxX:
            return False
        for j in choices:
            if j not in temp:
                return False

        temp = ''
        count = 0
        for j in range(dim):
            if board[j][dim-1-j] == 'X':
                count += 1
            temp += board[j][dim-1-j]
        if count > maxX:
            return False
        for j in choices:
            if j not in temp:
                return False   

    return True

def init_board():
    # yo fuck Python and its initialization man
    board = []
    for i in range(dim):
        board.append([])
        for j in range(dim):
            board[i].append(choices)
    # optimize
    for i in range(dim):
        # head // j = 0
        for j in range(dim-len(choices)+2, dim):
            board[i][j] = board[i][j].replace(constraint[0][i][0],'')
            board[j][i] = board[j][i].replace(constraint[1][i][0],'')
        # toe // j = 1
        for j in range(0, len(choices)-2):
            board[i][j] = board[i][j].replace(constraint[0][i][1],'')
            board[j][i] = board[j][i].replace(constraint[1][i][1],'')
    # check only case
    cancel_all(board)
    return board

def cancel_all(board):
    changed = True
    while changed:
        changed = False
        # cancel first rows/columns - as nothing can occur before the constraint
        # check rows
        for i in range(dim):
            pos = 0
            if constraint[0][i][0] != '':
                while True:
                    if pos == dim:
                        break
                    if board[i][pos] == constraint[0][i][0]:
                        break
                    if board[i][pos] == 'X':
                        pos += 1
                    else:
                        for j in choices:
                            if j != 'X' and j != constraint[0][i][0]:
                                board[i][pos] = board[i][pos].replace(j,'')
                        break
            pos = -1
            if constraint[0][i][1] != '':
                while True:
                    if pos == -1-dim:
                        break
                    if board[i][pos] == constraint[0][i][1]:
                        break
                    if board[i][pos] == 'X':
                        pos -= 1
                    else:
                        for j in choices:
                            if j != 'X' and j != constraint[0][i][1]:
                                board[i][pos] = board[i][pos].replace(j,'')
                        break

        # check columns
        for i in range(dim):
            pos = 0
            if constraint[1][i][0] != '':
                while True:
                    if pos == dim:
                        break
                    if board[i][pos] == constraint[1][i][0]:
                        break
                    if board[pos][i] == 'X':
                        pos += 1
                    else:
                        for j in choices:
                            if j != 'X' and j != constraint[1][i][0]:
                                board[pos][i] = board[pos][i].replace(j,'')
                        break
            pos = -1
            if constraint[1][i][1] != '':
                while True:
                    if pos == -1-dim:
                        break
                    if board[pos][i] == constraint[1][i][1]:
                        break
                    if board[pos][i] == 'X':
                        pos -= 1
                    else:
                        for j in choices:
                            if j != 'X' and j != constraint[1][i][1]:
                                board[pos][i] = board[pos][i].replace(j,'')
                        break

        # check for assignments: if a row/column has only one box to put a char,
        # then that box gets that char
        for c in choices:
            if c != 'X':
                # check rows
                for i in range(dim):
                    count = 0
                    lastAppeared = -1
                    for j in range(dim):
                        if c in board[i][j]:
                            if c == board[i][j]:
                                count = -1
                                break
                            count += 1
                            lastAppeared = j
                    if count == 1:
                        changed = True
                        board[i][lastAppeared] = c
                        optimize(board,[i,lastAppeared])
                        cancel_all(board)
                        return

                # check columns
                for i in range(dim):
                    count = 0
                    lastAppeared = -1
                    for j in range(dim):
                        if c in board[j][i]:
                            if c == board[j][i]:
                                count = -1
                                break
                            count += 1
                            lastAppeared = j
                    if count == 1:
                        changed = True
                        board[lastAppeared][i] = c
                        optimize(board,[lastAppeared,i])
                        cancel_all(board)
                        return

                # check diagonals
                if diag:
                    count = 0
                    lastAppeared = -1
                    for j in range(dim):
                        if c in board[j][j]:
                            if c == board[j][j]:
                                count = -1
                                break
                            count += 1
                            lastAppeared = j
                    if count == 1:
                        changed = True
                        board[lastAppeared][lastAppeared] = c
                        optimize(board,[lastAppeared,lastAppeared])
                        cancel_all(board)
                        return

                    count = 0
                    lastAppeared = -1
                    for j in range(dim):
                        if c in board[j][dim-1-j]:
                            if c == board[j][dim-1-j]:
                                count = -1
                                break
                            count += 1
                            lastAppeared = j
                    if count == 1:
                        changed = True
                        board[lastAppeared][dim-1-lastAppeared] = c
                        optimize(board,[lastAppeared,dim-1-lastAppeared])
                        cancel_all(board)
                        return
            else:
                # check rows
                for i in range(dim):
                    xcount = 0
                    for j in range(dim):
                        if board[i][j] == c:
                            xcount += 1
                    if xcount == maxX:
                        for j in range(dim):
                            if board[i][j] != c:
                                board[i][j] = board[i][j].replace(c,'')

                # check columns
                for i in range(dim):
                    xcount = 0
                    for j in range(dim):
                        if board[j][i] == c:
                            xcount += 1
                    if xcount == maxX:
                        for j in range(dim):
                            if board[j][i] != c:
                                board[j][i] = board[j][i].replace(c,'')

                # check diagonals
                if diag:
                    xcount = 0
                    for j in range(dim):
                        if board[j][j] == c:
                            xcount += 1
                    if xcount == maxX:
                        for j in range(dim):
                            if board[j][j] != c:
                                board[j][j] = board[j][j].replace(c,'')

                    xcount = 0
                    for j in range(dim):
                        if board[j][dim-1-j] == c:
                            xcount += 1
                    if xcount == maxX:
                        for j in range(dim):
                            if board[j][dim-1-j] != c:
                                board[j][dim-1-j] = board[j][dim-1-j].replace(c,'')

def optimize(board, coord):
    if not is_legit(board):
        reset_board(board)
        return
    # check top
    if board[coord[0]][coord[1]] != '':
        # check rows
        if board[coord[0]][coord[1]] == constraint[0][coord[0]][0]:
            for j in range(coord[1]):
                board[coord[0]][j] = 'X'
        if board[coord[0]][coord[1]] == constraint[0][coord[0]][1]:
            for j in range(coord[1]+1,dim):
                board[coord[0]][j] = 'X'
        # check columns
        if board[coord[0]][coord[1]] == constraint[1][coord[1]][0]:
            for i in range(coord[0]):
                board[i][coord[1]] = 'X'
        if board[coord[0]][coord[1]] == constraint[1][coord[1]][1]:
            for i in range(coord[0]+1,dim):
                board[i][coord[1]] = 'X'

    # clear all
    if len(board[coord[0]][coord[1]]) != 1:
        raise ValueError('Not supposed to reduce a nonsingular string!')
    if board[coord[0]][coord[1]] != 'X':
        for i in range(dim):
            if i != coord[0]:
                board[i][coord[1]] = board[i][coord[1]].replace(board[coord[0]][coord[1]],'')
        for j in range(dim):
            if j != coord[1]:
                board[coord[0]][j] = board[coord[0]][j].replace(board[coord[0]][coord[1]],'')
        if diag:
            if coord[0] == coord[1]:
                for i in range(dim):
                    if i != coord[0]:
                        board[i][i] = board[i][i].replace(board[coord[0]][coord[1]],'')
            if coord[0]+coord[1] == dim-1:
                for i in range(dim):
                    if i != coord[0]:
                        board[i][dim-1-i] = board[i][dim-1-i].replace(board[coord[0]][coord[1]],'')

    # TODO: unoptimized as cancel all board rather than
    # just one character and its corresponding columns and rows
    cancel_all(board)

def printOut(board):
    for i in range(dim):
        for j in range(dim):
            if board[i][j] == 'X':
                print '.',
            else:
                print board[i][j],
        print

def mass_optimize(board):
    if not is_legit(board):
        reset_board(board)
        return
    for i in range(dim):
        for j in range(dim):
            if len(board[i][j]) == 1 and board[i][j] != 'X':
                optimize(board,[i,j])

def if_print(board):
    for i in range(dim):
        for j in range(dim):
            if answer[i][j] not in board[i][j]:
                print "halted at",
                print (i+1),
                print (j+1)
                return False
    return True

def solve(shit_to_solve):
    # print len(shit_to_solve)
    board = shit_to_solve.pop()
    # do_print = if_print(board)
    # do_print = is_legit(board)
    do_print = False
    
    if do_print:
        print board
    
    if is_legit(board):
        global trials_count
        trials_count += 1
        
        if is_deadend(board):
            global solutions_count
            solutions_count += 1
            print "SOLUTION FOUND! --- after",
            print trials_count,
            print "trials"
            printOut(board)
            print
            
            # fuck all other solutions
            # shit_to_solve[:] = []
            # return
        else:
            if has_no_null(board):
                minc = min_coord(board)
                if minc == None:
                    return

                if do_print:
                    print minc
                    print 'org', board

                new_board = deepcopy(board)
                new_board[minc[0]][minc[1]] = new_board[minc[0]][minc[1]][0]
                board[minc[0]][minc[1]] = board[minc[0]][minc[1]][1:]
                cancel_all(board)
                cancel_all(new_board)
                mass_optimize(board)
                mass_optimize(new_board)

                if do_print:
                    print 'new', new_board
                    print 'old', board
                
                shit_to_solve.append(board)
                shit_to_solve.append(new_board)       

def main():
    shit_to_solve = [init_board()]
    while len(shit_to_solve) != 0:
    # for i in range(2):
        solve(shit_to_solve)
    print "total number of solutions:", solutions_count
    print "total number of trials:", trials_count

def test():
    tic = default_timer()
    # insert code to test here
    main()
    # end of code insertion
    toc = default_timer()
    print "time taken in seconds:", toc-tic

# main()
# test()

def test2():
    board = init_board()
    board[0][0] = 'A'
    board[1][0] = 'C'
    board[2][0] = 'X'
    board[2][1] = 'X'
    board[2][2] = 'A'
    board[4][0] = 'X'
    board[6][0] = 'E'
    cancel_all(board)
    mass_optimize(board)
    cancel_all(board)
    printOut(board)
