
chosen_features = [ 
	'dsport', 'proto', 'state', 'dur', 'sbytes', 'dbytes', 'sttl', 'dttl', 'service', 'Sload', 'Dload', 'swin', 'stcpb', 'dtcpb', 'smeansz', 'dmeansz', 'trans_depth', 'res_bdy_len', 'Sjit', 'Djit', 'Stime', 'Sintpkt', 'Dintpkt', 'tcprtt', 'is_sm_ips_ports', 'ct_state_ttl', 'ct_flw_http_mthd', 'ct_srv_src', 'ct_dst_ltm', 'ct_src_ltm' 
]

discarded_features = [
	'SrcAddr','Sport','DstAddr','SrcLoss','DstLoss',
	'SrcPkts','DstPkts','DstWin','LastTime','SynAck',
]

proto_mapper = {
	'-': 106,
	
	'udp': 0, 'arp': 1, 'tcp': 2, 'ospf': 3, 'icmp': 4, 'igmp': 5, 'sctp': 6, 'udt': 7, 'sep': 8, 'sun-nd': 9, 'swipe': 10, 'mobile': 11, 'pim': 12, 
	'rtp': 13,'ipnip': 14, 'ip': 15, 'ggp': 16, 'st2': 17, 'egp': 18, 'cbt': 19, 'emcon': 20, 'nvp': 21, 'igp': 22, 'xnet': 23, 'argus': 24, 
	'bbn-rcc': 25, 'chaos': 26, 'pup': 27, 'hmp': 28, 'mux': 29, 'dcn': 30, 'prm': 31, 'trunk-1': 32, 'xns-idp': 33, 'trunk-2': 34, 'leaf-1': 35, 'leaf-2': 36, 
	'irtp': 37, 'rdp': 38, 'iso-tp4': 39, 'netblt': 40, 'mfe-nsp': 41, 'merit-inp': 42, '3pc': 43, 'xtp': 44, 'idpr': 45, 'tp++': 46, 'ddp': 47, 'idpr-cmtp': 48, 
	'ipv6': 49, 'il': 50, 'idrp': 51, 'ipv6-frag': 52, 'sdrp': 53, 'ipv6-route': 54, 'gre': 55, 'rsvp': 56, 'mhrp': 57, 'bna': 58, 'esp': 59, 'i-nlsp': 60, 
	'narp': 61, 'ipv6-no': 62, 'tlsp': 63, 'skip': 64, 'ipv6-opts': 65, 'any': 66, 'cftp': 67, 'sat-expak': 68, 'kryptolan': 69, 'rvd': 70, 'ippc': 71, 'sat-mon': 72, 
	'ipcv': 73, 'visa': 74, 'cpnx': 75, 'cphb': 76, 'wsn': 77, 'pvp': 78, 'br-sat-mon': 79, 'wb-mon': 80, 'wb-expak': 81, 'iso-ip': 82, 'secure-vmtp': 83, 'vmtp': 84, 
	'vines': 85, 'ttp': 86, 'nsfnet-igp': 87, 'dgp': 88, 'tcf': 89, 'eigrp': 90, 'sprite-rpc': 91, 'larp': 92, 'mtp': 93, 'ax.25': 94, 'ipip': 95, 'micp': 96, 
	'aes-sp3-d': 97, 'encap': 98, 'etherip': 99, 'pri-enc': 100, 'gmtp': 101, 'pnni': 102, 'ifmp': 103, 'aris': 104, 'qnx': 105, 'scps': 107, 'snp': 108, 
	'ipcomp': 109, 'compaq-peer': 110, 'ipx-n-ip': 111, 'vrrp': 112, 'zero': 113, 'pgm': 114, 'iatp': 115, 'ddx': 116, 'l2tp': 117, 'srp': 118, 'stp': 119, 'smp': 120, 
	'uti': 121, 'sm': 122, 'ptp': 123, 'fire': 124, 'crtp': 125, 'isis': 126, 'crudp': 127, 'sccopmce': 128, 'sps': 129, 'pipe': 130, 'iplt': 131, 'unas': 132, 
	'fc': 133, 'ib': 134,
}

state_mapper = {
	'-': 10,

	'CON': 0, 'INT': 1, 'FIN': 2, 'URH': 3, 'REQ': 4, 'ECO': 5, 'RST': 6, 'CLO': 7, 'TXD': 8, 'URN': 9, 'ACC': 11, 'PAR': 12,
	'MAS': 13, 'TST': 14, 'ECR': 15,
}

service_mapper = {
	'-': 1,

	'dns': 0, 'http': 2, 'smtp': 3, 'ftp-data': 4, 'ftp': 5, 'ssh': 6, 'pop3': 7, 'snmp': 8, 'ssl': 9, 'irc': 10, 'radius': 11, 'dhcp': 12,
}

dsport_mapper = {
	# '-': -1,
	'http': 80,
	'https': 443, 
	'rmtcfg' : 1236,
}