# traceroute-mapping
This is a python script which will allow the user to understand the route taking by network traffic, it is advanced version of traceroute linux terminal command

```
usage: python traceroute_info.py 8.8.8.8
```
output
```
traceroute to 8.8.8.8 (8.8.8.8), 64 hops max, 52 byte packets
103.94.136.42	Cochin	AS23860 Alliance Broadband Services Pvt. Ltd.
103.94.136.41	Cochin	AS23860 Alliance Broadband Services Pvt. Ltd.
202.78.239.62	Kolkata	AS23860 Alliance Broadband Services Pvt. Ltd.
108.170.253.97	Mountain View	AS15169 Google LLC
108.170.253.113	Mountain View	AS15169 Google LLC
108.170.253.97	Mountain View	AS15169 Google LLC
216.239.43.209	Broken Arrow	AS15169 Google LLC
72.14.237.165	Mountain View	AS15169 Google LLC
216.239.42.237	Broken Arrow	AS15169 Google LLC
8.8.8.8	Mountain View	AS15169 Google LLC
```

Now, connect to any VPN service and execute the same command and see the difference
output, ( proton VPN )
```
traceroute to 8.8.8.8 (8.8.8.8), 64 hops max, 52 byte packets
209.58.147.203	Dallas	AS394380 Leaseweb USA, Inc.
209.58.147.252	Houston	AS394380 Leaseweb USA, Inc.
209.58.147.253	Houston	AS394380 Leaseweb USA, Inc.
209.58.159.6	Dallas	AS394380 Leaseweb USA, Inc.
209.58.159.4	Dallas	AS394380 Leaseweb USA, Inc.
209.58.159.6	Dallas	AS394380 Leaseweb USA, Inc.
31.31.38.180	Amsterdam	xe-2-0-0.bb10.dal-10.leaseweb.net
31.31.38.182	Amsterdam	xe-2-0-0.bb11.dal-10.leaseweb.net
31.31.38.180	Amsterdam	xe-2-0-0.bb10.dal-10.leaseweb.net
31.31.34.76	Amsterdam	xe-2-0-3.bb10.dal-10.leaseweb.net
31.31.34.87	Washington, D.C.	te-3-1.bb02.wdc-01.leaseweb.net
31.31.34.87	Washington, D.C.	te-3-1.bb02.wdc-01.leaseweb.net
206.55.196.29	Wilmington	
108.170.246.1	Mountain View	AS15169 Google LLC
206.55.196.29	Wilmington	
216.239.54.107	Broken Arrow	AS15169 Google LLC
108.170.235.113	Mountain View	AS15169 Google LLC
209.85.143.231	New York City	AS15169 Google LLC
72.14.234.135	Mountain View	AS15169 Google LLC
8.8.8.8	Mountain View	AS15169 Google LLC
```

