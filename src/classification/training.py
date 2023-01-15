import pickle
import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier

from utils import chooseMostAccurateModel

# Extracting data

assets_folder = './../../assets/'
models_folder = assets_folder + 'models/'


data = pd.read_csv(assets_folder + 'UNSW-NB15-preprocessed.csv',low_memory=False)

X, labels, classes = data.iloc[:, 1:30], data.iloc[:, 32], data.iloc[:, 31]

# return only the  
classes_attacks = classes[labels != 0]

classifiers = {
	'randomforest' : RandomForestClassifier(),
    'kneighbors': KNeighborsClassifier(),
    'mlp': MLPClassifier(),
}

print('\nBinary classifier')

model, _ = chooseMostAccurateModel(X, labels, classifiers=classifiers, n_rounds=20, plot=True)
pickle.dump(model, open(models_folder + 'binary_model', 'wb'))

print('\nMulticlass classifier')

X_attacks = X[labels != 0]

model, _ = chooseMostAccurateModel(X_attacks, classes_attacks, classifiers=classifiers, n_rounds=20, plot=True)
pickle.dump(model, open(models_folder + 'multiclass_model', 'wb'))

