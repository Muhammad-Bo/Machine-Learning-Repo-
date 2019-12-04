from random import seed
from random import random
from csv import reader
from math import exp
import sys

pos = 0
counter = 0


def NN(number_of_inputs, number_of_hidden, number_of_outputs):
    nueral_network = list()
    hidden_layer = [{'weights': [random() for item in range(number_of_inputs + 1)]} for item in range(number_of_hidden)]
    nueral_network.append(hidden_layer)
    output_layer = [{'weights': [random() for i in range(number_of_hidden + 1)]} for i in range(number_of_outputs)]
    nueral_network.append(output_layer)
    return nueral_network


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


def prediction_nn(neural_network, dt_rows):
    calculated_outputs = fw_propagate(neural_network, dt_rows)
    return calculated_outputs.index(max(calculated_outputs))


def Neuron_Active(weight_param, input):
    activation = weight_param[-1]
    for item in range(len(weight_param) - 1):
        activation += weight_param[item] * input[item]
    return activation


def sigmoid_func(nuerons_activations):
    return 1 / (1 + exp(-nuerons_activations))


def fw_propagate(neural_network, row_tuple):
    inputs = row_tuple
    for LAYER in neural_network:
        input_new = []
        for NEURON in LAYER:
            do_activation = Neuron_Active(NEURON['weights'], inputs)
            NEURON['output'] = sigmoid_func(do_activation)
            input_new.append(NEURON['output'])
        inputs = input_new
    return inputs


def derivative_sigmoid(output_param):
    return output_param * (1 - output_param)


def bp_propagate(neural_network, target):
    for item in reversed(range(len(neural_network))):
        LAYERS = neural_network[item]
        ERROR = list()
        if item != len(neural_network) - 1:
            for j in range(len(LAYERS)):
                error = 0.0
                for neuron in neural_network[item + 1]:
                    error += (neuron['weights'][j] * neuron['delta'])
                ERROR.append(error)
        else:
            for j in range(len(LAYERS)):
                neuron = LAYERS[j]
                ERROR.append(target[j] - neuron['output'])
        for j in range(len(LAYERS)):
            neuron = LAYERS[j]
            neuron['delta'] = ERROR[j] * derivative_sigmoid(neuron['output'])


def weight_update(neural_network, dt_row, learning_rate):
    for item in range(len(neural_network)):
        inputs = dt_row[:-1]
        if item != 0:
            inputs = [neuron['output'] for neuron in neural_network[item - 1]]
        for neuron in neural_network[item]:
            for j in range(len(inputs)):
                neuron['weights'][j] += learning_rate * neuron['delta'] * inputs[j]
            neuron['weights'][-1] += learning_rate * neuron['delta']


def neural_network_train(neural_network, train_dataset, learning_rates, number_of_iteration, number_of_output):
    for iteration in range(number_of_iteration):
        cumulative_error = 0
        for row in train_dataset:
            outputs = fw_propagate(neural_network, row)
            expected = [0 for j in range(number_of_output)]
            expected[row[-1]] = 1
            cumulative_error += sum([(expected[k] - outputs[k]) ** 2 for k in range(len(expected))])
            bp_propagate(neural_network, expected)
            weight_update(neural_network, row, learning_rates)
       # print('>#Iteration=%d, LR=%.3f, Calculated_Error=%.3f' % (iteration, learning_rates, cumulative_error))


def pointer(list_a):
    global pos
    global counter
    if pos < list_a.index(max(list_a)):
        counter = 0
        pos = list_a.index(max(list_a))
#        print("This is Pos:", pos)
    elif pos == list_a.index(max(list_a)):
        counter += 1

    if counter == 11:
        print("Need To be Stopped")
        for layer in network:
            print(layer)

        calculated_test = []
        expected_test = []
        score_test = []
        test_b(test_set, calculated_test, expected_test, score_test)
        sys.exit()


def find_min_max_dt(datasets):
    minimum_maxmimum = list()
    status = [[min(columns_dt), max(columns_dt)] for columns_dt in zip(*datasets)]
    return status


def test_a(dataset, expected_list, calculated_list,score_store):
    score = 0
    for row in dataset:
        prediction = prediction_nn(network, row)
        expected_list.append(row[-1])
        calculated_list.append(prediction)

    for items in range(len(calculated_list)):
        if expected_list[items] == calculated_list[items]:
            score += 1

    if len(expected_list) == len(calculated_list):
        print(len(expected_list))
        print("Final Score:{} ".format(score/len(expected_list)))

    score_store.append(score/len(expected_list))
    pointer(score_store)

def test_b(dataset, expected_list, calculated_list,score_store):
    score = 0
    print("This is For test set")
    for layer in network:
        print(layer)
    for row in dataset:
        prediction = prediction_nn(network, row)
        expected_list.append(row[-1])
        calculated_list.append(prediction)

    for items in range(len(calculated_list)):
        if expected_list[items] == calculated_list[items]:
            score += 1

    if len(expected_list) == len(calculated_list):
        print(len(expected_list))
        print("Final Score:{} ".format(score/len(expected_list)))

    score_store.append(score/len(expected_list))
#


def normalization_dt(datasets, minimum_max):
    for row in datasets:
        for item in range(len(row) - 1):
            row[item] = (row[item] - minimum_max[item][0]) / (minimum_max[item][1] - minimum_max[item][0])


def split_list(a_list):
    half = len(a_list)//2
    return a_list[:half], a_list[half:]

seed(1)
# dataset = [
#     [1, 1, 22, 22, 22, 19, 18, 14, 49.895756, 17.775994, 5.27092, 0.771761, 0.018632, 0.006864, 0.003923, 0.003923,
#      0.486903, 0.100025, 1, 0],
#     [1, 1, 24, 24, 22, 18, 16, 13, 57.709936, 23.799994, 3.325423, 0.234185, 0.003903, 0.003903, 0.003903, 0.003903,
#      0.520908, 0.144414, 0, 0],
#     [1, 1, 62, 60, 59, 54, 47, 33, 55.831441, 27.993933, 12.687485, 4.852282, 1.393889, 0.373252, 0.041817, 0.007744,
#      0.530904, 0.128548, 0, 1],
#     [1, 1, 55, 53, 53, 50, 43, 31, 40.467228, 18.445954, 9.118901, 3.079428, 0.840261, 0.272434, 0.007653, 0.001531,
#      0.483284, 0.11479, 0, 0],
#     [1, 1, 44, 44, 44, 41, 39, 27, 18.026254, 8.570709, 0.410381, 0, 0, 0, 0, 0, 0.475935, 0.123572, 0, 1],
#     [1, 1, 44, 43, 41, 41, 37, 29, 28.3564, 6.935636, 2.305771, 0.323724, 0, 0, 0, 0, 0.502831, 0.126741, 0, 1],
#     [1, 0, 29, 29, 29, 27, 25, 16, 15.448398, 9.113819, 1.633493, 0, 0, 0, 0, 0, 0.541743, 0.139575, 0, 1],
#     [1, 1, 6, 6, 6, 6, 2, 1, 20.679649, 9.497786, 1.22366, 0.150382, 0, 0, 0, 0, 0.576318, 0.071071, 1, 0],
#     [1, 1, 22, 21, 18, 15, 13, 10, 66.691933, 23.545543, 6.151117, 0.496372, 0, 0, 0, 0, 0.500073, 0.116793, 0, 1]]

seed(1)
# load and prepare data
import_file = 'train0.csv'
dataset = import_csv(import_file)
for item in range(len(dataset[0]) - 1):
    floatization(dataset, item)
# convert class column to integers
Intization(dataset, len(dataset[0]) - 1)
minmax = find_min_max_dt(dataset)
normalization_dt(dataset, minmax)

# #### Importing Validation Test ######
import_file_1 = 'valid.csv'
validation = import_csv(import_file_1)
for item in range(len(validation[0]) - 1):
    floatization(validation, item)
# convert class column to integers
Intization(validation, len(validation[0]) - 1)
minmax = find_min_max_dt(validation)
normalization_dt(validation, minmax)

# #################
# #### Importing Validation Test ######
import_file_1 = 'test_01.csv'
test_set = import_csv(import_file_1)
for item in range(len(test_set[0]) - 1):
    floatization(test_set, item)
# convert class column to integers
Intization(test_set, len(test_set[0]) - 1)
minmax = find_min_max_dt(test_set)
normalization_dt(test_set, minmax)
########
score = 0
number_of_inputs = len(dataset[0]) - 1
number_of_outputs = len(set([row[-1] for row in dataset]))
network = NN(number_of_inputs, 1, number_of_outputs)
expected_list = []
calculated_list = []
i = 0
score_store = []
while i < 600:
    neural_network_train(network, dataset, 0.1, i, number_of_outputs)
    test_a(dataset, calculated_list, expected_list, score_store)
    expected_list = []
    calculated_list = []
    i += 1

print(score_store)

        # for layer in network:
        #     print(layer)

    # for row in dataset:
    #     prediction = prediction_nn(network, row)
    #     expected_list.append(row[-1])
    #     calculated_list.append(prediction)
    #        # print((row[-1], prediction), file=open("training_value1.txt", "a"))
    #     #print("##################### End of Epoch{}############ on Training".format(item), file=open("training_value.txt", "a"))
    #     # for row in validation:
    #     #     prediction = prediction_nn(network, row)
    #     #     print((row[-1], prediction), file=open("validation_value1.txt", "a"))
    #     #print("##################### End of Epoch{}############ on Validation".format(item), file=
    #
    # for items in range(len(calculated_list)):
    #     print(items)
    #     if expected_list[items] == calculated_list[items]:
    #         score += 1
    #
    # if len(expected_list) == len(calculated_list):
    #     print(len(expected_list))
    #     print("Final Score:{} ".format(score))




# print("This is Expected List: ", expected_list)
# print("This Calculated List:", calculated_list)
# print(len(expected_list))
# print(len(calculated_list))
#
# print(expected_list[0])
# print(calculated_list[0])
# for item in range(len(expected_list)):
#     if expected_list[item] == calculated_list[item]:
#         score += 1
#
# print("Final Accuracy Result", score)