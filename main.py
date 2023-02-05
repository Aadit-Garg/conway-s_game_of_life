import numpy as np
from random import randint as rn
from time import sleep as sl
import os

new_lis = [[0 for i in range(10)] for i in range(10)]
lis = [[0 for i in range(10)] for i in range(10)]
new_lis = np.array(new_lis)
lis = np.array(lis)


def make_alive(x, y):
  lis[y][x] = 1
  new_lis[y][x] = 1


def if_state(x, y):
  try:
    if new_lis[y][x] == 1:
      return 1
    else:
      return 0
  except:
    return 0


def check_neighbour(x, y):
  count = 0
  count += if_state(x - 1, y - 1)
  count += if_state(x, y - 1)
  count += if_state(x + 1, y - 1)
  count += if_state(x - 1, y)
  count += if_state(x + 1, y)
  count += if_state(x - 1, y + 1)
  count += if_state(x, y + 1)
  count += if_state(x + 1, y + 1)
  return count


def check(x, y):
  if lis[y][x] == 0:
    count = check_neighbour(x, y)
    if count == 3:
      lis[y][x] = 1
  elif lis[y][x] == 1:
    count = check_neighbour(x, y)
    if count < 2:
      lis[y][x] = 0
    elif count < 4:
      lis[y][x] = 1
    else:
      lis[y][x] = 0


for i in range(0, rn(10, 20)):
  make_alive(rn(0, 9), rn(0, 9))
# make_alive(1, 2)
# print(*lis, sep="\n")
for i in range(50):
  os.system("clear")

  for y in range(10):
    for x in range(10):
      check(x, y)
  # sl(0.1)
  print(f"GENRATION: {i+1}")
  print(*lis, sep="\n")
  # sl(0.1)
  print("")
  new_lis = np.copy(lis)
  sl(0.5)
  if 1 not in lis:
    print(f"life ended at gen: {i}")
    break
