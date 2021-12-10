import random
import math
import numpy as np


def clockwise_angle(v1, v2):
    '''vector angle for polar coordinate'''
    vec_x = v1.getX() - v2.getX()
    vec_y = v1.getY() - v2.getY()
    theta = np.arctan2(vec_y, vec_x)
    theta = theta if theta > 0 else 2 * np.pi + theta
    return theta * 180 / np.pi


def split_list(items, m):
    n = int(math.ceil(len(items) / m))
    return [items[i:i+n] for i in range(0, len(items), n)]


def double_rand(start, end):
    '''generate random values'''
    start_pos, end_pos = 0, 0
    while (start_pos >= end_pos):
        start_pos = random.randint(start, end)
        end_pos   = random.randint(start, end)
    return start_pos, end_pos
