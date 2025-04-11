def hanoi(n, source, aux, target):
  '''
  Solves the game Towers of Hanoi by applying the pattern of how to move three disks
  
  :param n: number of disks in play
  :param source: the post that the disks begin on
  :param aux: the post that is neither the starting post nor the ending rod
  :param target: the post that the disks should end on
  '''
  if n == 1:
    print(f'move from post {source} to post {target}')
  else:
    hanoi(n-1, source, target, aux)
    hanoi(1, source, aux, target)
    hanoi(n-1, aux, source, target)

hanoi(4,'1','2','3')
