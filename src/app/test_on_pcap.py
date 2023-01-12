
import pickle
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

# data = pd.read_csv("./../assets/CC22-final-only-attacks.csv").iloc[:, 1:30]
data = pd.read_csv("./../assets/CC22-final.csv").iloc[:, 1:30]

loaded_model, accuracy = pickle.load(open("./../assets/models/binary_model", 'rb'))
binary_labels = loaded_model.predict(data)
print(pd.DataFrame(binary_labels).value_counts())

chunks = np.array_split(binary_labels, len(binary_labels)//1000)

# initialize an empty dictionary to store the counts for each value in each chunk
counts = {val: [] for val in set(binary_labels)}

# iterate over the chunks
for i, chunk in enumerate(chunks):
    # get the counts of each value in the chunk
    chunk_counts = pd.value_counts(chunk)
    # add the counts to the dictionary
    for val in set(binary_labels):
        counts[val].append(chunk_counts.get(val, 0))

# create the bar chart
plt.bar(np.arange(len(chunks)), counts[0], align='center')
plt.bar(np.arange(len(chunks)), counts[1], align='center', bottom=counts[0])
plt.xticks(np.arange(len(chunks)), [f'Chunk {i+1}' for i in range(len(chunks))])
plt.legend(set(binary_labels))
plt.title('Chunk vs Value Counts')
plt.xlabel('Chunks')
plt.ylabel('Counts')
plt.show()


loaded_model = pickle.load(open("./../assets/models/multiclass_model", 'rb'))
labels = loaded_model.predict(data[binary_labels != 0])
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
for val in counts:
    plt.bar(np.arange(len(chunks)), counts[val], align='center', bottom=sum(sum(counts[prev_val]) for prev_val in counts if prev_val != val))

plt.xticks(np.arange(len(chunks)), [f'Chunk {i+1}' for i in range(len(chunks))])
plt.legend(counts.keys())
plt.title('Chunk vs Value Counts')
plt.xlabel('Chunks')
plt.ylabel('Counts')
plt.show()