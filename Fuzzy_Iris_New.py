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
        for item in range(len(row)):
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


def find_max(matrix):
    return matrix.argmax()


# load and prepare data
import_file = 'Iris_dt.csv'
dataset = import_csv(import_file)
# for row in range(len(dataset)):
#     print(len(dataset[row]))
#     del dataset[row][len(dataset[row])-1]


for item in range(len(dataset[0]) - 1):
    floatization(dataset, item)
# convert class column to integers
B = array(dataset)
compare = B[:, 4]
compare = compare.astype(np.int)
dataset_f = B[0:len(B), 0:4]
dataset_f = dataset_f.astype(np.float)
dataset_f = dataset_f.tolist()
# Intization(dataset, len(dataset[0]) - 1)
minmax = find_min_max_dt(dataset_f)
print(dataset_f)
print("This is Min:{}".format(minmax))
normalization_dt(dataset_f, minmax)
print(dataset_f)
n = len(dataset_f)
matrix = np.zeros((n, 4))  # Pre-allocate matrix
for i in range(1, n):
    matrix[i, :] = [rules(dataset_f[i], "R1"), rules(dataset_f[i], "R2"), rules(dataset_f[i], "R3"), rules(dataset_f[i], "R4")]

print("#####" * 20)
print("This is Matrix After Applying Rules:")
print(matrix)
print("#####" * 20)
# print(matrix)
result = np.apply_along_axis(find_max, 1, matrix)
for i in range(len(result)):
    result[i] += 1
# print(result)

# print("###" * 40)
# print("Printing Dataset:")
# print(dataset_f)
# print("###" * 40)
# for i in range(100):
#     print(dataset_f[i])
#     RES = rules(dataset_f[i], "R1")
#     RES_2 = rules(dataset_f[i], "R2")
#     RES_3 = rules(dataset_f[i], "R3")
#     RES_4 = rules(dataset_f[i], "R4")
#     print("This is i{}".format(i))
#     print(RES, RES_2, RES_3, RES_4)
#     print("#####" * 20)

# dataset_f = copy.deepcopy(dataset)
final_result = []
for i in range(len(result)):
    if result[i] == 1:
        final_result.append(2)
    elif result[i] == 2:
        final_result.append(1)
    elif result[i] == 3:
        final_result.append(3)
    elif result[i] == 4:
        final_result.append(2)
print("####" * 20)
#print("This is Final Vector of Output after Applying Fussy classifier:")
#print(final_result)
print("####" * 20)
match = 0
print(compare)
print(final_result)
for i in range(len(final_result)):
    if final_result[i] == compare[i]:
        match += 1


print("Final Match on Dataset Is:{}".format(match/150))
