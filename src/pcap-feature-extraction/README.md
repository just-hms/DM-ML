# Features name in `ra` vs the dataset

|`ra`			|dataset		|to_extract		| used	|		
|-				|-				|-				|	-	|	
|`saddr`     	|`srcip`		|`saddr`		|		|
|`sport`		|`sport`		|`sport`	 	|		|
|`daddr`     	|`dstip`		|`daddr`	 	|		|
|`-`		  	|`dsport`		|`dport`	 	|	v	|
|`proto`		|`proto`		|`proto`	 	|	v	|
|`state`		|`state`		|`state`	 	|	v	|
|`dur`			|`dur`			|`dur`	 		|	v	|
|`sbytes`		|`sbytes`		|`sbytes`	 	|	v	|
|`dbytes`		|`dbytes`		|`dbytes`	 	|	v	|
|`sttl`			|`sttl`			|`sttl`	 		|	v	|
|`dttl`			|`dttl`			|`dttl`	 		|	v	|
|`sloss`		|`sloss`		|`sloss`	 	|		|
|`dloss`		|`dloss`		|`dloss`	 	|		|
|`-`		  	|`service`		|`dport`		|	v	|
|`dload`		|`Dload`		|`dload`	 	|	v	|
|`sload`		|`Sload`		|`sload`	 	|	v	|
|`spkts`		|`Spkts`		|`spkts`	 	|		|
|`dpkts`		|`Dpkts`		|`dpkts`	 	|		|
|`swin`			|`swin`			|`swin`	 		|	v	|
|`dwin`			|`dwin`			|`dwin`	 		|		|
|`stcpb`		|`stcpb`		|`stcpb`	 	|	v	|
|`dtcpb`		|`dtcpb`		|`dtcpb`	 	|	v	|
|`smeansz`		|`smeansz`		|`smeansz`	 	|	v	|
|`dmeansz`		|`dmeansz`		|`dmeansz`	 	|	v	|
|`trans`		|`trans_depth`	|`trans`		|	v	|
|`appbytes`		|`res_bdy_len`	|`psize`    	|	v	|
|`sjit`			|`Sjit`			|`sjit`	 		|	v	|
|`djit`			|`Djit`			|`djit`	 		|	v	|
|`stime`		|`Stime`		|`stime`	 	|	v	|
|`ltime`		|`Ltime`		|`ltime`	 	|		|
|`sintpkt`		|`Sintpkt`		|`sintpkt`	 	|	v	|
|`dintpkt`		|`Dintpkt`		|`dintpkt`	 	|	v	|
|`tcprtt`		|`tcprtt`		|`tcprtt`	 	|	v	|
|`synack`		|`synack`		|`synack`	 	|		|
|`ackdat`		|`ackdat`		|`ackdat`	 	|		|


## aggregated

|to_extract				| used	|		
|-						|	-	|	
|`is_sm_ips_ports`		|	v	|									
|`ct_state_ttl`			|	v	|	
|`ct_srv_src`			|	v	|
|`ct_dst_ltm`			|	v	|
|`ct_src_ltm`			|	v	|       



