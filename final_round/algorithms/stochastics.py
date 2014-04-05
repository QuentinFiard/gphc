import numpy as np


def multinomial(probs):
    '''
    Multinomial variable

    Parameters
    ----------
    probs: 1D array-like
       weight of each class

    '''

    cs = np.cumsum(probs)  # CDF
    cs /= cs.max()  # normalization for stochasticity

    return np.min(np.nonzero(np.random.rand() <= cs))


def sample_neighbor(intersect_idx, roads_dict, max_cost):
  n = neighbor_roads(intersect_idx, roads_dict)
  n = [x for x in n if x.cost <= max_cost]
  if n:
    scores = [1. / x.distance for x in n]
    # scores = np.reciprocal(scores)  # XXX risky business here
    return n[multinomial(scores)]
