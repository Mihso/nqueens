from pprint import pprint

board = []

n = 4

rows = n
col = n

queensPosition=[]

def create_empty_board(n):
    board = []
    rows = n
    col = n
    for r in range(rows):
        column = []
        for c in range(col):
            column.append('None')
        board.append(column)
    return board

def check_if_safe(b, crow, col):
    for row in range(len(b)):
        if b[row][col] != 'None':
            return False
        else:
            for q in queensPosition:
                for n in range(len(b)*len(b[row])):
                    if crow == (q['row'] + n) and col == (q['col'] + n):
                        return False
                for q in queensPosition:
                    for n in range(len(b)*len(b[row])):
                        if crow == (q['row'] + n) and col == (q['col'] - n):
                            return False
                for q in queensPosition:
                    for n in range(len(b)*len(b[row])):
                        if crow == (q['row'] - n) and col == (q['col'] + n):
                            return False
                for q in queensPosition:
                    for n in range(len(b)*len(b[row])):
                        if crow == (q['row'] - n) and col == (q['col'] - n):
                            return False
    return True

def place_piece(b, row, col):
    b[row][col] = "queen"
    queensPosition.append({"row":row, "col":col})

def attempt_solution(b, first_row):
    for row in range(len(b)):
        place_piece(b, first_row, 0)
    for row in range(len(b)):
        for col in range(len(b)):
            if check_if_safe(b, row, col):
                place_piece(b, row, col)
                break

def find_solutions(n):
    solution = False
    attempt = 0
    while solution == False:
        board = create_empty_board(n)
        attempt_solution(board, attempt)
        pprint(board, width =80)
        overallFound = True
        for row in range(len(board)):
            found = False
            for col in range(len(board)):
                if board[row][col] != 'None':
                    found = True
            if found == False:
                overallFound = False
        if overallFound == False:
            attempt +=1
            print("next attempt")
        else:
            pprint(board, width=80)
            return (queensPosition)
        if attempt >= len(board):
            return None

print(find_solutions(4))
# create_empty_board(4)
# attempt_solution(1)
# pprint(board, width=80)
