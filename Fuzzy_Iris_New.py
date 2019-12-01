from numpy import *
import numpy as np
from csv import reader



def membership_features(x, type):
    # print(x)
    if type == "short":
        if x < 0:
            return 0
        elif 0 <= x <= 0.6:
            return (1 - (x / 0.6))
        elif x > 0.6:
            return 0
    if type == "medium":
        if x < 0:
            return 0
        elif 0 <= x <= 0.6:
            return x / 0.6
        elif 0.6 < x <= 1:
            return ((1 + 0.6 / 0.4) - (x / 0.4))
        elif x > 1:
            return 0
    if type == "long":
        if x < 0.6:
            return 0
        elif 0.6 <= x <= 1:
            return ((x / 0.4) - ((1 / 0.4) - 1))
        elif x > 1:
            return 0


def rules(row_date, rule_number):
    print(row_date[0], row_date[1], row_date[2], row_date[3])
    if rule_number == "R1":
        result = min(max(membership_features(row_date[0], "short"), membership_features(row_date[0], "long")),
                     max(membership_features(row_date[1], "medium"), membership_features(row_date[1], "long")),
                     max(membership_features(row_date[2], "medium"), membership_features(row_date[2], "long")),
                     membership_features(row_date[3], "medium"))
    elif rule_number == "R2":
        result = min(max((membership_features(row_date[2], "short"), membership_features(row_date[2], "medium"))),
                     membership_features(row_date[3], "short"))

    elif rule_number == "R3":
        result = min(max(membership_features(row_date[1], "short"), membership_features(row_date[1], "medium")),
                     membership_features(row_date[2], "long"),
                     membership_features(row_date[3], "long"))

    elif rule_number == "R4":
        result = min(membership_features(row_date[0], "medium"),
                     max(membership_features(row_date[1], "short"), membership_features(row_date[1], "medium")),
                     membership_features(row_date[2], "short"),
                     membership_features(row_date[3], "long"))
    return result


def normalization_dt(datasets, minimum_max):
    for row in datasets:
        for item in range(len(row) - 1):
            row[item] = (row[item] - minimum_max[item][0]) / (minimum_max[item][1] - minimum_max[item][0])


def find_min_max_dt(datasets):
    minimum_maxmimum = list()
    status = [[min(columns_dt), max(columns_dt)] for columns_dt in zip(*datasets)]
    # return status[0:len(status)-1:]
    return status


def import_csv(import_csv):
    training_data = list()
    with open(import_csv, 'r') as dt:
        csv_reader = reader(dt)
        for item in csv_reader:
            if not item:
                continue
            training_data.append(item)
    return training_data


def floatization(data_set, column):
    for row in data_set:
        row[column] = float(row[column].strip())


def Intization(data_set, columns):
    cl_target = [row[columns] for row in data_set]
    unique_mod = set(cl_target)
    search = dict()
    for i, value in enumerate(unique_mod):
        search[value] = i
    for row in data_set:
        row[columns] = search[row[columns]]
    return search


def normalization_dt_2(datasets):
    for row in datasets:
        print(len(row))


# load and prepare data
import_file = 'iris.csv'
dataset = import_csv(import_file)
# for row in range(len(dataset)):
#     print(len(dataset[row]))
#     del dataset[row][len(dataset[row])-1]


for item in range(len(dataset[0]) - 1):
    floatization(dataset, item)
# convert class column to integers
B = array(dataset)
dataset_f = B[0:30, 0:4]
dataset_f = dataset_f.astype(np.float)
dataset_f = dataset_f.tolist()
# Intization(dataset, len(dataset[0]) - 1)
minmax = find_min_max_dt(dataset_f)

normalization_dt(dataset_f, minmax)
# print("###" * 40)
# print("Printing Dataset:")
# print(dataset_f)
# print("###" * 40)
for i in range(15):
    print(dataset_f[i])
    RES = rules(dataset_f[i], "R1")
    RES_2 = rules(dataset_f[i], "R2")
    RES_3 = rules(dataset_f[i], "R3")
    RES_4 = rules(dataset_f[i], "R4")
    print("This is i{}".format(i))
    print(RES, RES_2, RES_3, RES_4)
    print("#####" * 20)

# dataset_f = copy.deepcopy(dataset)
