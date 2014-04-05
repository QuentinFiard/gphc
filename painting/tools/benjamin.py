def get_all_squares(n, m):
    squares = []
    for i in range(n):
        for j in range(m):
            x, y = 0, 0
            while (i+x) < n and (j+y) < m:
                square = ((i, j), (i+x, j+y))
                squares.append(square)
                x += 2
                y += 2
    return squares
