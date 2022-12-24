# plot histogram
nominal_features = ["proto", "state", "service"]

for att in nominal_features:
    plt.figure()
    plt.hist(data[att].astype(str), bins = len(data[att].value_counts()))
    plt.ylabel('Occurrences')
    plt.xlabel(att)
    plt.title(f'histogram of {att} attribute')
	plt.xticks(rotation=45)

