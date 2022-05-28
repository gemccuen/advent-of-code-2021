def check_board(board, drawn_nums):
    #Check rows
    winning = []
    for row in board:
        for col in row:
            if col in drawn_nums:
                winning.append(col)
            else:
                winning = []
                break
            if len(winning) == 5:
                return board

    #Check cols
    winning = []
    for col in range(5):
        for row in range(5):
            if board[row][col] in drawn_nums:
                winning.append(board[row][col])
            else:
                winning = []
                break
            if len(winning) == 5:
                return board


with open("input.txt", 'r') as infile:
    nums = [int(num) for num in infile.readline().split(",")]
    drawn_nums = []
    boards = []
    current_num = 0
    board_sum = 0

    while infile.readline() != "":
        board = []
        for i in range(5):
            raw_row = infile.readline().strip().split(" ")
            row = []
            for j in raw_row:
                try:
                    row.append(int(j))
                except ValueError:
                    pass
            board.append(row)
        boards.append(board)
    
    for num in nums:
        current_num = num
        drawn_nums.append(num)
        for i, board in enumerate(boards):
            result = check_board(board, drawn_nums)
            if result:
                del boards[i]
                if len(boards) != 0:
                    result = None
                else:
                    break
        if result:
            break

    for row in result:
        for col in row:
            if col not in drawn_nums:
                board_sum += col
    
print(board_sum * current_num)