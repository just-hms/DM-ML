import pyshark

# Open the PCAP file using pyshark
capture = pyshark.FileCapture('out_2.pcap')

def get_state(packet : any):
	
	if packet.proto == "TCP":
		b_flags = int(packet.tcp.flags, 16)

		if b_flags & 16 != 0:
			return "ACK"
		if b_flags & 2 != 0:
			return "SYN"
		if b_flags & 1 != 0:
			return "FIN"
		if b_flags & 32 != 0:
			return "URG"
		if b_flags & 8 != 0:
			return "PSH"
		if b_flags & 8 != 0:
			return "RST"
	
	return "-"
	
# Iterate over each packet in the PCAP file
for packet in capture:
	# Extract the srcip, sport, dstip, and dsport values
	srcip = packet.ip.src
	sport = packet.tcp.srcport
	dstip = packet.ip.dst
	dsport = packet.tcp.dstport

	# Extract the proto value
	proto = packet.transport_layer

	state = get_state(packet)

	# Extract the dur value
	dur = packet.frame_info.time_relative

	# Extract the sbytes and dbytes values
	sbytes = packet.tcp.len
	dbytes = packet.ip.len

	# Extract the sttl and dttl values
	sttl = packet.ip.ttl
	dttl = packet.ip.ttl

	# Extract the sloss and dloss values
	sloss = packet.tcp.nxtseq
	dloss = packet.tcp.ack

	# Extract the service value
	if packet.highest_layer == "HTTP":
		service = "http"
	elif packet.highest_layer == "FTP":
		service = "ftp"
	elif packet.highest_layer == "SMTP":
		service = "smtp"
	elif packet.highest_layer == "SSH":
		service = "ssh"
	elif packet.highest_layer == "DNS":
		service = "dns"
	elif packet.highest_layer == "FTP-DATA":
		service = "ftp-data"
	elif packet.highest_layer == "IRC":
		service = "irc"
	else:
		service = "-"

	# Extract the Sload and Dload values
	Sload = packet.tcp.window_size
	Dload = packet.tcp.window_size_value

	# Extract the Spkts and Dpkts values
	Spkts = packet.tcp.nxtseq
	Dpkts = packet.tcp.ack

	# Extract the swin and dwin values
	swin = packet.tcp.window_size
	dwin = packet.tcp.window_size_value

	# Extract the stcpb and dtcpb values
	stcpb = packet.tcp.seq
	dtcpb = packet.tcp.ack

	# TODO : Extract the smeansz and dmeansz values
	# smeansz = packet.tcp.segment_length
	# dmeansz = packet.tcp.segment_length

	# Extract the trans_depth value
	# trans_depth = packet.http.request_number

	# Extract the res_bdy_len value
	# res_bdy_len = packet.http.response_body_len

	# Extract the Sjit and Djit values
	try:
		Sjit = packet.tcp.tcp_analysis_acks_frame
		Djit = packet.tcp.tcp_analysis_ack_rtt
	except:
		pass

	# Extract the Stime and Ltime values
	Stime = packet.sniff_time
	Ltime = packet.frame_info.time_epoch

	# Extract the Sintpkt and Dintpkt values
	Sintpkt = packet.tcp.time_delta
	Dintpkt = packet.tcp.time_delta

	# Extract the tcprtt, synack, and ackdat values
	try:
		tcprtt = packet.tcp.analysis_rtt
		synack = packet.tcp.time_relative_to_previous_frame
		ackdat = packet.tcp.time_relative_to_first_request
	except:
		pass