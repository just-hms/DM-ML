# salame

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

from sklearn.metrics import accuracy_score
from pandas import read_csv
from numpy import ravel
from sklearn.neural_network import MLPClassifier

import pandas as pd

data = read_csv(
	'UNSW-NB15/UNSW-NB15_1.csv', 
	low_memory=False,
	names= [
		'srcip','sport','dstip','dsport','proto','state','dur','sbytes',
		'dbytes','sttl','dttl','sloss','dloss','service','Sload','Dload',
		'Spkts','Dpkts','swin','dwin','stcpb','dtcpb','smeansz',
		'dmeansz','trans_depth','res_bdy_len','Sjit','Djit','Stime','Ltime','Sintpkt',
		'Dintpkt','tcprtt','synack','ackdat','is_sm_ips_ports','ct_state_ttl','ct_flw_http_mthd',
		'is_ftp_login','ct_ftp_cmd','ct_srv_src','ct_srv_dst','ct_dst_ltm','ct_src_ltm',
		'ct_src_dport_ltm','ct_dst_sport_ltm','ct_dst_src_ltm','attack_cat','Label',
	]
)

# data = data.sample(70_000)

nominals = [
	'srcip',
	'dstip',
	'proto',
	'state',
	'service',
	'attack_cat',
]

for n in nominals:
	tmp, indexes = pd.factorize(data[n])
	data[n] = tmp

data['sport'] = data['sport'].apply(int, base=16)
data['dsport'] = data['dsport'].apply(int, base=16)

training_data, testing_data, training_labels, testing_labels = \
	train_test_split(
		data.iloc[:, 0:46], 
		data.iloc[:, 48]
	)

mlp = MLPClassifier(random_state=0)

model1 = RandomForestClassifier().fit(
		training_data, 
		ravel(training_labels)
	)

labels1 = model1.predict(testing_data)
score1 = accuracy_score(ravel(testing_labels), labels1)

print(score1)
