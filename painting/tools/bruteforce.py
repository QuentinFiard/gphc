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
        res.append((i, j))
  return Set(res)


def GetWhitePixels(image):
  res = []
  for i in xrange(len(image)):
    for j in xrange(len(image[i])):
      if not image[i][j]:
        res.append((i, j))
  return Set(res)


def SquareArea(square):
  return (square[1][0] - square[0][0]) * (square[1][1] - square[0][1])

MAX_LEVEL = 5

def BruteForceAux(to_draw, possible_squares, white_pixels, empty_pixels, previous_blocks, level=0):
  if len(to_draw) == 0:
    to_erase = white_pixels.difference(empty_pixels)
    return previous_blocks, list(to_erase)
  # Pick a pixel.
  pixel = random.sample(to_draw, 1)[0]
  # Get all the squares that cover it.
  squares = SquaresForPixel(possible_squares, pixel)
  # Speed-up: if white_pixels is empty, only preserve the largest square.
  if len(white_pixels) == 0:
    largest_square = squares[0]
    for square in squares:
      if SquareArea(square) > SquareArea(largest_square):
        largest_square = square
    squares = [largest_square]
  # Only keep the smallest one if we reached the recursion limit.
  if level > MAX_LEVEL:
    smallest_square = squares[0]
    for square in squares:
      if SquareArea(square) < SquareArea(smallest_square):
        smallest_square = square
    squares = [smallest_square]
  best_value = None
  res_for_best_square = None
  for square in squares:
    possible_squares_new = possible_squares.copy()
    to_draw_new = to_draw.copy()
    empty_pixels_new = empty_pixels.copy()
    previous_blocks_new = previous_blocks[:]
    previous_blocks_new.append(square)
    possible_squares_new.discard(square)
    top_left = square[0]
    x = top_left[0]
    y = top_left[1]
    for i in xrange(square[0][0], square[1][0] + 1):
      for j in xrange(square[0][1], square[1][1] + 1):
        to_draw_new.discard((i, j))
        empty_pixels_new.discard((i, j))
    res = BruteForceAux(
        to_draw_new, possible_squares_new, white_pixels, empty_pixels_new, previous_blocks_new, level+1)
    value = len(res[0]) + len(res[1])
    if not best_value or best_value > value:
      best_value = value
      res_for_best_square = res
  return res_for_best_square


def memoize(f):
    """ Memoization decorator for functions taking one or more arguments. """
    class memodict(dict):
        def __init__(self, f):
            self.f = f
        def __call__(self, *args):
            return self[args]
        def __missing__(self, key):
            ret = self[key] = self.f(*key)
            return ret
    return memodict(f)


@memoize
def BruteForce(image):
  squares = Set(bj.get_all_squares(len(image), len(image[0])))
  empty_pixels = []
  for i in xrange(len(image)):
    for j in xrange(len(image[0])):
      empty_pixels.append((i, j))
  empty_pixels = Set(empty_pixels)
  to_draw = GetBlackPixels(image)
  white_pixels = GetWhitePixels(image)
  return BruteForceAux(to_draw, squares, white_pixels, empty_pixels, [])


if __name__ == '__main__':
  image = [[True, True, True, False], [True, True, True, False],
           [True, True, True, False], [False, False, False, False]]
  res = BruteForce(image)
  print res
