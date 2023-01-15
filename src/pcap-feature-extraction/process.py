import pandas as pd
import numpy as np
from mapper import *

data = pd.read_csv('./extracted.csv',low_memory=False)

# If source and destination IP addresses equal and port numbers are equal then, this variable takes value 1 else 0
data['is_sm_ips_ports'] = data.apply(lambda row: row['Sport'] == row['Dport'] and row['SrcAddr'] == row['DstAddr'], axis=1)

# No. for each state (6) according to specific range of values for source/destination time to live (10) (11).
data['ct_state_ttl'] = 0

# No. of connections that contain the same service (14) and source address (1) in 100 connections according to the last time (26).
ct_srv_src = np.zeros(len(data), dtype=object) 
# No. of connections of the same destination address (3) in 100 connections according to the last time (26).
ct_dst_ltm = np.zeros(len(data), dtype=object) 
# No. of connections of the same source address (1) in 100 connections according to the last time (26).
ct_src_ltm = np.zeros(len(data), dtype=object)

last_dst_ips = np.empty(100, dtype=object)
last_src_ips = np.empty(100, dtype=object)
last_services = np.empty(100, dtype=object)

for i, x in data.iterrows():
	last_dst_ips[i%100] = x['DstAddr']
	last_src_ips[i%100] = x['SrcAddr'] 
	last_services[i%100] = x['Dport']

	for j in range(0,100):
		if last_dst_ips[j] == x['DstAddr']:
			ct_srv_src[i]+=1
			
		if last_src_ips[j] == x['SrcAddr']:
			ct_dst_ltm[i]+=1
		if last_services[j] == x['Dport'] and last_src_ips[j] == x['SrcAddr'] :
			ct_src_ltm[i]+=1

data['ct_src_ltm'] = ct_src_ltm
data['ct_dst_ltm'] = ct_dst_ltm
data['ct_srv_src'] = ct_srv_src

data.info()

# Data preprocessing

data.drop(inplace=True, columns=discarded_features)

# rename using original name scheme
data.columns = chosen_features

# map nominal features

data['proto'] = data['proto'].apply(lambda x : proto_mapper['-'] if not x in proto_mapper else proto_mapper[x])
data['state'] = data['state'].apply(lambda x : state_mapper['-'] if not x in state_mapper else state_mapper[x])
data['service'] = data['service'].apply(lambda x : service_mapper['-'] if not x in service_mapper else service_mapper[x])

data['dsport'] = data['dsport'].apply(lambda x : x if not x in dsport_mapper else dsport_mapper[x])

data.fillna(-1, inplace=True)
data.info()

data.to_csv('./processed.csv')