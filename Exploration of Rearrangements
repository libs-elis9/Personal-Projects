from matplotlib import pyplot as plt

def rearrange(a: callable, L: float, N: int) -> tuple[list[float], list[int]]:
    """
    Finds a rearrangement of a whose alternating series converges to L

    :param a: a sequence function
    :param L: a limit
    :param N: the number of terms to rearrange

    :return: a tuple containing the following:
        a list of the rearranged terms
        a list of the rearranged indices
    """
    seq = [(-1)**n * a(n) for n in range(N)]
    pos_ind = 0
    neg_ind = 1
    current = 0
    terms = []
    ind = []
    for i in range(N):
      if current < L:
        if pos_ind >= N:
          break
        current += seq[pos_ind]
        ind.append(pos_ind)
        terms.append(seq[pos_ind])
        pos_ind += 2

      else:
        if neg_ind >= N:
          break
        current += seq[neg_ind]
        ind.append(neg_ind)
        terms.append(seq[neg_ind])
        neg_ind += 2

    return terms, ind

def plot_rearrangement(a: callable, limits: list[float], N: int) -> None:
    """
    Plots the partial sums of a alongside its rearrangements converging to each L in limits

    :param a: a sequence function
    :param L: a list of limits
    :param N: the number of terms to rearrange
    """
    for L in limits:
      x, y = rearrange(a, L, N)
      A = [0]
      for t in x:
         A.append(t + A[-1])
      plt.plot(A,".-", label=f'$L = {L}$')

    B = [0]
    for n in range(N):
      bn = (-1)**n * a(n)
      B.append(bn + B[-1])
    plt.plot(B, ".-", label=r"$(-1)^na(n)$")
    plt.title("Rearrangements")
    plt.xlabel(r'Terms $(n)$')
    plt.ylabel(r'Partial Sums')
    plt.legend()

plot_rearrangement(lambda n: 1/(n+1), [0, 1, -1], 100)
