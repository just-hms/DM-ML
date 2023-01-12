# LAUNCH using linux

if [[ $# -ne 1 ]] && [[ $# -ne 2 ]] ; then 
	echo "wrong format!"
	exit
fi

argus -r $1 -w filename.argus

list="saddr, sport, daddr, dport, proto, state, dur, sbytes, dbytes, sttl, dttl, \
	sloss, dloss, dport, sload, dload, spkts, dpkts, swin, dwin, stcpb, dtcpb, smeansz, \
	dmeansz, trans, appbytes, sjit, djit, stime, ltime, sintpkt, dintpkt, tcprtt, synack, ackdat"

if [[ $# -eq 2 ]] ; then 
	ra -r filename.argus -c ',' -u -s $list > $2
else
	ra -r filename.argus -c ',' -u -s $list
fi

rm filename.argus

