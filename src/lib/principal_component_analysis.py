import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

def PCA_extract(data, verbose=False):
	
	pca = PCA(n_components=0.90, svd_solver='full')

	X, labels, classes = data.drop(["Label", "attack_cat"], axis=1), data.Label, data.attack_cat

	# scale data
	X = StandardScaler().fit_transform(X)

	pca.fit_transform(X)

	components = pca.components_

	if verbose:
		table = pd.DataFrame(
			pca.explained_variance_ratio_, 
			columns = ['Explained_variance_ratio']
		)

		print(table * 100)

	return X, labels, classes, components
