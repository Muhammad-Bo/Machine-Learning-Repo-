import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
import pandas as pd
import random
import warnings

warnings.filterwarnings("ignore", category=UserWarning)

edges = [(0, 1, {'weight': 2}),
         (0, 4, {'weight': 2}),
         (0, 19, {'weight': 1}),
         (1, 3, {'weight': 5}),
         (1, 19, {'weight': 4}),
         (1, 2, {'weight': 2}),
         (1, 5, {'weight': 3}),
         (2, 5, {'weight': 7}),
         (2, 18, {'weight': 9}),
         (3, 4, {'weight': 1}),
         (3, 9, {'weight': 7}),
         (4, 10, {'weight': 3}),
         (5, 11, {'weight': 2}),
         (5, 12, {'weight': 7}),
         (5, 16, {'weight': 3}),
         (5, 21, {'weight': 1}),
         (6, 10, {'weight': 8}),
         (6, 9, {'weight': 5}),
         (6, 7, {'weight': 2}),
         (7, 8, {'weight': 4}),
         (7, 15, {'weight': 1}),
         (8, 10, {'weight': 5}),
         (9, 14, {'weight': 3}),
         (11, 13, {'weight': 4}),
         (13, 14, {'weight': 1}),
         (14, 15, {'weight': 1}),
         (12, 13, {'weight': 5}),
         (12, 22, {'weight': 3}),
         (12, 20, {'weight': 1}),
         (22, 13, {'weight': 6}),
         (20, 22, {'weight': 2}),
         (21, 20, {'weight': 5}),
         (16, 17, {'weight': 4}),
         (17, 18, {'weight': 2})]

G = nx.Graph()
G.add_edges_from(edges)
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos)
nx.draw_networkx_edges(G, pos)
nx.draw_networkx_labels(G, pos)
plt.show()
# print(G.get_edge_data('S', 'V'))

q = np.matrix(np.zeros(shape=(23, 23)))

q[0, 1] = 2
q[0, 4] = 2
q[0, 19] = 1
q[1, 0] = 2
q[1, 2] = 2
q[1, 3] = 5
q[1, 5] = 3
q[2, 1] = 2
q[2, 5] = 7
q[2, 18] = 9
q[3, 1] = 5
q[3, 4] = 1
q[3, 9] = 7
q[4, 0] = 2
q[4, 3] = 1
q[4, 10] = 3
q[5, 1] = 3
q[5, 2] = 7
q[5, 11] = 2
q[5, 12] = 7
q[5, 16] = 3
q[5, 21] = 1
q[6, 7] = 2
q[6, 9] = 5
q[6, 10] = 8
q[7, 6] = 2
q[7, 8] = 4
q[7, 15] = 1
q[8, 7] = 4
q[8, 10] = 5
q[9, 3] = 7
q[9, 6] = 5
q[9, 14] = 3
q[10, 4] = 3
q[10, 6] = 8
q[10, 8] = 5
q[11, 5] = 2
q[11, 13] = 4
q[12, 5] = 7
q[12, 13] = 5
q[12, 20] = 1
q[12, 22] = 3
q[13, 11] = 4
q[13, 12] = 5
q[13, 14] = 1
q[13, 22] = 6
q[14, 9] = 3
q[14, 13] = 1
q[14, 15] = 1
q[15, 7] = 1
q[15, 14] = 1
q[16, 5] = 3
q[16, 17] = 4
q[17, 16] = 4
q[17, 18] = 2
q[18, 2] = 9
q[18, 17] = 2
q[19, 0] = 1
q[20, 12] = 1
q[20, 21] = 5
q[20, 22] = 2
q[21, 5] = 1
q[21, 20] = 5
q[22, 12] = 3
q[22, 13] = 6
q[22, 20] = 2

r = np.matrix(np.zeros(shape=(23, 23)))
r[2, 5] = 100
r[16, 5] = 100
r[1, 5] = 100
r[11, 5] = 100
r[12, 5] = 100
r[21, 5] = 100


def node_next(start, er):
    random_number_value = random.uniform(0, 1)
    if random_number_value < er:
        selected_samples = G[start]
    else:
        selected_samples = np.where(q[start,] == np.max(q[start, ]))[1]
    next_node = int(np.random.choice(selected_samples, 1))
    return next_node


def update_Q_learning(node1, node2, lr, discount):
    index_maximum = np.where(q[node2,] == np.max(q[node2, ]))[1]
    if index_maximum.shape[0] > 1:
        index_maximum = int(np.random.choice(index_maximum, size=1))
    else:
        index_maximum = int(index_maximum)
    max_value = q[node2, index_maximum]
    q[node1, node2] = int((1 - lr) * q[node1, node2] + lr * (r[node1, node2] + discount * max_value))


def learn_phase(er, lr, discount):
    for i in range(4000):
        starting_point = np.random.randint(0, 23)
        next_node = node_next(starting_point, er)
        update_Q_learning(starting_point, next_node, lr, discount)


def finding_shortest_path(begin, end):
    path = [begin]
    next_node = np.argmax(q[begin, ])
    path.append(next_node)
    while next_node != end:
        next_node = np.argmax(q[next_node, ])
        path.append(next_node)
    return path


print("###" * 20)
print(pd.DataFrame(q))
print("###" * 20)
learn_phase(0.5, 0.8, 0.8)
print(finding_shortest_path(8, 5))
