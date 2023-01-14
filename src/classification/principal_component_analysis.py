from matplotlib.pyplot import boxplot
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

def PCA_extract(data):
	
	pca = PCA(n_components=0.90, svd_solver='full')
	sc = StandardScaler()

	X = sc.fit_transform(data)
	X = pca.fit_transform(X)

	table = pd.DataFrame(
		pca.explained_variance_ratio_, 
		columns = ['Explained_variance_ratio']
	)

	print(table * 100)

	comps = pd.DataFrame(pca.components_, columns = data.columns)

	# print(comps)

	print(comps.apply(lambda x: abs(x)).mean().sort_values(ascending = False))

	boxplot(comps.apply(lambda x: abs(x)))


	return X, pca, sc
