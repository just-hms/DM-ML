import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

def PCA_extract(X):
	
	pca = PCA(n_components=0.90, svd_solver='full')
	sc = StandardScaler()

	X = sc.fit_transform(X)
	X = pca.fit_transform(X)

	table = pd.DataFrame(
		pca.explained_variance_ratio_, 
		columns = ['Explained_variance_ratio']
	)

	print(table * 100)

	return X, pca, sc
