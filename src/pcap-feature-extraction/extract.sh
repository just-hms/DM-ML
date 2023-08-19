# requirements
# - #! linux
# - argus
# - ra

# usage
# ./extract.sh file.pcap > file.csv

if [[ $# -ne 1 ]] ; then 
	echo 'wrong format!'
	exit
fi

argus -r $1 -w filename.argus

list='saddr, sport, daddr, dport, proto, state, dur, sbytes, dbytes, sttl, dttl, \
	sloss, dloss, dport, sload, dload, spkts, dpkts, swin, dwin, stcpb, dtcpb, smeansz, \
	dmeansz, trans, appbytes, sjit, djit, stime, ltime, sintpkt, dintpkt, tcprtt, synack, ackdat'

ra -r filename.argus -c ',' -u -s $list
rm filename.argus

