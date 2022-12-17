# x=1
# while [ $x -le 1000000000000000 ]
# do
#   	echo "Welcome $x times"
#   	x=$(( $x + 1 ))
# done

argus -r out_2.pcap -w filename.argus
ra -r filename.argus -u -s srcip,sport,dstip,dsport,proto,state,dur,sbytes,dbytes,sttl,dttl,sloss,dloss,service,Sload,Dload,Spkts,Dpkts,swin,dwin,stcpb,dtcpb,smeansz,dmeansz,trans_depth,res_bdy_len >> kek.txt


