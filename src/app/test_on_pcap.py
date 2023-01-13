
import pickle
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

def plot(labels):
    
    print(pd.DataFrame(labels).value_counts())
    print()

    chunks = np.array_split(labels, len(labels)//500)

    # initialize an empty dictionary to store the counts for each value in each chunk
    counts = {val: [] for val in set(labels)}

    # iterate over the chunks
    for i, chunk in enumerate(chunks):
        # get the counts of each value in the chunk
        chunk_counts = pd.value_counts(chunk)
        # add the counts to the dictionary
        for val in set(labels):
            counts[val].append(chunk_counts.get(val, 0))

    # create the stacked bar chart
    bar_width = 1 / (len(set(labels)) + 1)

    for i, val in enumerate(counts):
        plt.bar(np.arange(len(chunks)) + bar_width * i, counts[val], align='center', width=bar_width, label=val)

    plt.xticks(np.arange(len(chunks)), [f'{i+1}' for i in range(len(chunks))])
    plt.legend()
    plt.title('Attacks in time')
    plt.xlabel('Chunks')
    plt.ylabel('Counts')
    # plt.yscale('log')  # this line makes the y-axis logarithmic
    plt.show()

learning_data = pd.read_csv("./../assets/UNSW-NB15-preprocessed.csv")
learning_data = learning_data[learning_data['Label'] == 0]

only_bots_data = pd.read_csv("./../assets/CC22-final-also-bots.csv").iloc[:, 1:30]
also_attacks_data = pd.read_csv("./../assets/CC22-final-also-attacks.csv").iloc[:, 1:30]

float_features_to_scale = [
    "dur", 
    "sbytes", "dbytes", 
    "Sload", "Dload", 
    "swin",  
    "Sjit", "Djit", 
    "Stime", 
    "Sintpkt", "Dintpkt", 
    "tcprtt",
]

int_features_to_scale = [
    "smeansz", 
    "dmeansz",
    "ct_state_ttl", 
    "ct_flw_http_mthd", 
    "ct_srv_src", 
    "ct_dst_ltm",
]


for col in float_features_to_scale:
    
    avg = sum(only_bots_data[col])/len(only_bots_data)
    avg_learning = sum(learning_data[col])/len(only_bots_data)

    ratio = avg / avg_learning

    print(ratio)

    only_bots_data[col] *= ratio 
    also_attacks_data[col] *= ratio

for col in int_features_to_scale:
    
    avg = sum(only_bots_data[col])/len(only_bots_data)
    avg_learning = sum(learning_data[col])/len(only_bots_data)

    ratio = avg / avg_learning

    print(ratio)

    only_bots_data[col] = round(ratio * only_bots_data[col])
    also_attacks_data[col] = round(ratio * also_attacks_data[col])


loaded_model = pickle.load(open("./../assets/models/binary_model", 'rb'))
binary_labels = loaded_model.predict(only_bots_data)
plot(binary_labels)


loaded_model = pickle.load(open("./../assets/models/multiclass_model", 'rb'))
labels = loaded_model.predict(only_bots_data[binary_labels != 0])
plot(labels)

print("ATTACKS")

loaded_model = pickle.load(open("./../assets/models/binary_model", 'rb'))
binary_labels = loaded_model.predict(also_attacks_data)
plot(binary_labels)


loaded_model = pickle.load(open("./../assets/models/multiclass_model", 'rb'))
labels = loaded_model.predict(also_attacks_data[binary_labels != 0])
plot(labels)