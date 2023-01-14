import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def plot(labels, title=''):
    
    print(pd.DataFrame(labels).value_counts())

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
    plt.title(title)
    plt.xlabel('Chunks')
    plt.ylabel('Counts')
    # plt.yscale('log')  # this line makes the y-axis logarithmic
    plt.show()