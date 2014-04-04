from sets import Set
import random

import benjamin as bj


def InSquare(square, pixel):
  return (square[0][0] <= pixel[0] and square[0][1] <= pixel[1] and
          square[1][0] >= pixel[0] and square[1][1] >= pixel[1])


def SquaresForPixel(list_squares, pixel):
  return filter(lambda square: InSquare(square, pixel), list_squares)


def GetBlackPixels(image):
  res = []
  for i in xrange(len(image)):
    for j in xrange(len(image[i])):
      if image[i][j]:
        res.append([i, j])
  return Set(res)


def GetWhitePixels(image):
  res = []
  for i in xrange(len(image)):
    for j in xrange(len(image[i])):
      if not image[i][j]:
        res.append([i, j])
  return Set(res)


def BruteForceAux(image, to_draw, possible_squares, empty_pixels):
  pass


def BruteForce(image):
  squares = bj.GetAllSquares(image)
  empty_pixels = [([i, j] for i in len(image)) ]
  white_pixels = GetWhitePixels(image)
  to_draw = GetBlackPixels(image)
  while len(to_draw) > 0:
    # Get next pixel to draw.
    pixel = random.sample(to_draw, 1)
    # Remove pixel from to_draw.




if __name__ == '__main__':
  assert InSquare([[0, 0], [1, 1]], [0.5, 0.5])
  assert not InSquare([[0, 0], [1, 1]], [1.5, 0.5])
  assert SquaresForPixel([[[0, 0], [1, 1]], [[2, 3], [1, 1]]],
                         [0.5, 0.5]) == [[[0, 0], [1, 1]]]
