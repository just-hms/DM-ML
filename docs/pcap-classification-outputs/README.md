# classification on `pcap` output

```sh

SCALE FACTORS

	dur 0.10890239321483493
	sbytes 0.05937458910275042
	dbytes 0.019195294402651504
	Sload 0.003990302362924578
	Dload 0.009235022017737944
	swin 718.3728728344787
	res_bdy_len 0.12638913034817256
	Sjit -0.0001807480743166005
	Djit -0.0003066024871620531
	Stime 0.3051080341915523
	Sintpkt -0.0015412293513965111
	Dintpkt -0.003723888346134258
	tcprtt 3.2800416921042737
	smeansz 0.20426072955147842
	dmeansz 0.10877900200409872
	trans_depth 2.755887300252313
	ct_state_ttl 0.00029806259314456036
	ct_flw_http_mthd -0.0
	ct_srv_src 3.1023816067553094
	ct_dst_ltm 7.142034691425571

PCAP BASELINE WITHOUT SCALING

	Attack    18654
	Normal     7564
	dtype: int64

	false positive [%]:  71.14959188343886

BASELINE

	Normal    25760
	Attack      458
	dtype: int64

	false positive [%]:  1.7468914486230835
	accuracy on baseline [%]:  98.25310855137693

ATTACKS

	Normal            11728
	Worms/Exploits      735
	Fuzzers/DoS         725
	dtype: int64
```