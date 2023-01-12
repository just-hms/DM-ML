flow_features = ['srcip','sport','dstip','dsport','proto']

base_features = [
	'state','dur','sbytes','dbytes','sttl','dttl','sloss',
	'dloss','service','Sload','Dload','Spkts','Dpkts'
]

content_features = [
	'swin','dwin','stcpb','dtcpb','smeansz',
	'dmeansz','trans_depth','res_bdy_len',
]

time_features = [
	'Sjit','Djit','Stime','Ltime','Sintpkt',
	'Dintpkt','tcprtt','synack','ackdat',
]

generated_features = [
	'is_sm_ips_ports','ct_state_ttl','ct_flw_http_mthd',
	'is_ftp_login','ct_ftp_cmd','ct_srv_src','ct_srv_dst','ct_dst_ltm','ct_src_ltm',
	'ct_src_dport_ltm','ct_dst_sport_ltm','ct_dst_src_ltm',
]

labels = [
	'attack_cat','Label',
]

nominals_features = [
	'srcip',
	'dstip',
	'proto',
	'state',
	'service',
]

chosen_features = [ "dsport", "proto", "state", "dur", "sbytes", "dbytes", "sttl", "dttl", "service", "Sload", "Dload", "swin", "stcpb", "dtcpb", "smeansz", "dmeansz", "trans_depth", "res_bdy_len", "Sjit", "Djit", "Stime", "Sintpkt", "Dintpkt", "tcprtt", "is_sm_ips_ports", "ct_state_ttl", "ct_flw_http_mthd", "ct_srv_src", "ct_dst_ltm", "ct_src_ltm" ]
