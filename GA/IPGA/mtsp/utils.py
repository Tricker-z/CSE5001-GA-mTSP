import math


def load_data(file_path_tmp):
    row_data = []
    with open(file_path_tmp, "r") as f:
        row_data = f.readlines()

    row_num = len(row_data) - 1

    iso_tuple_list = []
    for i in range(1, len(row_data)):
        item = row_data[i].strip().split(" ")
        iso_tuple_list.append((int(item[1]), int(item[2])))
    return iso_tuple_list


def cal_dis(t1, t2):
    return math.sqrt(sum([(a - b) ** 2 for (a, b) in zip(t1[:], t2[:])]))