def InSquare(square, pixel):
  return (square[0][0] <= pixel[0] and square[0][1] <= pixel[1] and
          square[1][0] >= pixel[0] and square[1][1] >= pixel[1])


def SquaresForPixel(list_squares, pixel):
  return filter(lambda square: InSquare(square, pixel), list_squares)


if __name__ == '__main__':
  assert InSquare([[0, 0], [1, 1]], [0.5, 0.5])
  assert not InSquare([[0, 0], [1, 1]], [1.5, 0.5])
  assert SquaresForPixel([[[0, 0], [1, 1]], [[2, 3], [1, 1]]],
                         [0.5, 0.5]) == [[[0, 0], [1, 1]]]
