chessboard = [input() for _ in range(8)]
rows = ["8","7","6","5","4","3","2","1"]
cols = ["a","b","c","d","e","f","g","h"]
for i in range(8):
    for j in range(8):
        if chessboard[i][j] == "*":
            print(cols[j]+rows[i])
            exit()