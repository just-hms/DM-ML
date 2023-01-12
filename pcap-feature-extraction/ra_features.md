## extracted

|ra			|dataset		|used			|
|-			|-				|-				|	
|saddr     	|srcip			|saddr			|	x
|sport		|sport			|sport	 		|	x
|daddr     	|dstip			|daddr	 		|	x
|\-		  	|dsport			|dport	 		|	v
|proto		|proto			|proto	 		|	v
|state		|state			|state	 		|	v
|dur		|dur			|dur	 		|	v
|sbytes		|sbytes			|sbytes	 		|	v
|dbytes		|dbytes			|dbytes	 		|	v
|sttl		|sttl			|sttl	 		|	v
|dttl		|dttl			|dttl	 		|	v
|sloss		|sloss			|sloss	 		|	x
|dloss		|dloss			|dloss	 		|	x
|\-		  	|service		|dport			|	v
|dload		|Dload			|dload	 		|	v
|sload		|Sload			|sload	 		|	v
|spkts		|Spkts			|spkts	 		|	x
|dpkts		|Dpkts			|dpkts	 		|	x
|swin		|swin			|swin	 		|	v
|dwin		|dwin			|dwin	 		|	x
|stcpb		|stcpb			|stcpb	 		|	v
|dtcpb		|dtcpb			|dtcpb	 		|	v
|smeansz	|smeansz		|smeansz	 	|	v
|dmeansz	|dmeansz		|dmeansz	 	|	v
|trans		|trans_depth	|trans			|	v
|\-	    	|res_bdy_len	|psize    		|	v
|sjit		|Sjit			|sjit	 		|	v
|djit		|Djit			|djit	 		|	v
|stime		|Stime			|stime	 		|	v
|ltime		|Ltime			|ltime	 		|	x
|sintpkt	|Sintpkt		|sintpkt	 	|	v
|dintpkt	|Dintpkt		|dintpkt	 	|	v
|tcprtt		|tcprtt			|tcprtt	 		|	v
|synack		|synack			|synack	 		|	x
|ackdat		|ackdat			|ackdat	 		|	x

##s aggregated

is_sm_ips_ports									v									
ct_state_ttl									v	
ct_srv_src										v
ct_dst_ltm										v
ct_src_ltm										v       