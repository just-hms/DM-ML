import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay, RocCurveDisplay, accuracy_score
from sklearn.model_selection import train_test_split


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

def chooseMostAccurateModel(X, labels, classifiers, n_rounds=20, plot=False):

	best_model_name = ""
	best_model = {}
	best_score = 0

	training_data, testing_data, training_labels, testing_labels = train_test_split(
		X,
		labels,
	)

	isMulticlass = len(set(labels)) > 2 

	#For each classifier, a model is created and tested
	for k, value in classifiers.items():
		
		model = value.fit(
			training_data,
			np.ravel(training_labels)
		)

		predicted_labels = model.predict(testing_data)

		score = accuracy_score(np.ravel(testing_labels), predicted_labels)

		print('  ', k, score)

		if score > best_score:
			best_model_name = k
			best_model = model
			best_score = score

		if plot:
			ConfusionMatrixDisplay.from_predictions(np.ravel(testing_labels), predicted_labels, normalize = 'true')
			plt.show()

			if not isMulticlass:
				RocCurveDisplay.from_predictions(np.ravel(testing_labels), predicted_labels)
				plt.show()

	print('chosen model: ', best_model_name)

	for i in range(1, n_rounds + 1):
		
		training_data, testing_data, training_labels, testing_labels = train_test_split(
			X,
			labels,
		)
		
		model = classifiers[best_model_name].fit(
			training_data,
			np.ravel(training_labels)
		)

		predicted_labels = model.predict(testing_data)

		score = accuracy_score(np.ravel(testing_labels), predicted_labels)

		print(i, 'score:', score)
		
		if score > best_score:
			best_model = model
			best_score = score

	print('best score: ', best_score)

	return best_model, best_score
