
import pickle
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt


def plot(labels):
    
    print(pd.DataFrame(labels).value_counts())

    chunks = np.array_split(labels, len(labels)//1000)

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
    plt.yscale('log')  # this line makes the y-axis logarithmic
    plt.show()

# data = pd.read_csv("./../assets/CC22-final-only-attacks.csv").iloc[:, 1:30]
data = pd.read_csv("./../assets/CC22-final-only-attacks.csv").iloc[:, 1:30]

loaded_model, accuracy = pickle.load(open("./../assets/models/binary_model", 'rb'))
binary_labels = loaded_model.predict(data)
plot(binary_labels)

loaded_model = pickle.load(open("./../assets/models/multiclass_model", 'rb'))
labels = loaded_model.predict(data[binary_labels != 0])

plot(labels)