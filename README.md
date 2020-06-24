# Network-Intrusion-Detection-System

## Table of Content
  * [Directory Tree](#directory-tree)
  * [BUSINESS CONTEXT](#business-context)
  * [BUSINESS PROBLEM](#business-problem)
  * [DATA AVAILABILITY](#data-availability)
  * [ATTACK CLASS](#attack-class)
  * [How to Use](#how-to-use)
  * [LICENSE](#license)

### Directory Tree

```
├── NSL_Dataset
│   ├── Test.txt
│   ├── Train.txt
├── results
│   ├── 2020-06-15 15_28_16-Window.png
│   ├── 2020-06-15 15_29_02-Window.png
│   ├── 2020-06-15 15_30_02-Window.png
│   ├── 2020-06-15 15_31_30-Window.png
│   ├── 2020-06-15 15_31_58-Window.png
│   ├── 2020-06-15 15_32_25-Window.png
├── static
│   ├── style.css
├── templates
│   ├── index.html
├── app.py
├── corrm.csv
├── Dockerfile
├── model.pkl
├── Network Intrusion Detection System.ipynb
├── num_summary.csv
├── pandas_profiling.html
├── requirements.txt
├── LICENSE
├── Procfile
├── README.md
```

### BUSINESS CONTEXT:

With the enormous growth of computer networks usage and the huge increase in the number of applications running on top of it, network secrity is becoming increasingly more important. All the computer systems suffer from security vulnerabilities which are both technically difficult and economically costly to be solved by the manufacturers. Therefore, the role of Intrusion Detection Systems (IDSs), as special purpose devices to detect anomalies and attacks in the network, is becoming more important. 

The research in the intrusion detection field has been mostly focused on a nomaly-based and misuse-based detection techniques for a long time. While misuse-based detction is generally favoured in commercial products due to its predictability and high accuracy, in academic research anomally detection is typically conceived as a more powerful method due to its theoretical potential for addressing novel attacks.

Conducting a through analysis of the recent research trend is anomaly detection, one will encounter several machine learning methods reported to have a very high detection rate of 98% while keeping the false alarm rate at 1%. However, when we look at the state of art IDS solutions and comercial tools, there is no evidence of using anomaly detection approaches, and practitioners still think that it is an immature technology. To find the reason of this contrast, lots of research was done in anomaly detection and considered various aspects such as learning, and detection approaches, training data sets, testing data sets, and evaluation methods.

### BUSINESS PROBLEM:

The task is to build network intrusion detection system to detect anamolies and attacks in the network. There are two problems.  

1) Binomial Classification: Activity is normal or attack 

2) Multinomial classification: Activity is normal or DOS or PROBE or R2L or U2R 

### DATA AVAILABILITY: 

This data is KDDCUP’99 data set, which is widely used as one of the few publicly available data sets for network-based anomaly detection systems.  
 
For more about data: http://www.unb.ca/cic/datasets/nsl.html 

#### LIST OF COLUMNS FOR THE DATA SET:

["duration","protocol_type","service","flag","src_bytes","dst_bytes","land", "wrong_fragment","urgent","hot","num_failed_logins","logged_in", "num_compromised","root_shell","su_attempted","num_root","num_file_creations", "num_shells","num_access_files","num_outbound_cmds","is_host_login", "is_guest_login","count","srv_count","serror_rate", "srv_serror_rate", "rerror_rate","srv_rerror_rate","same_srv_rate", "diff_srv_rate", 
"srv_diff_host_rate","dst_host_count","dst_host_srv_count","dst_host_same_srv_rate", "dst_host_diff_srv_rate","dst_host_same_src_port_rate", "dst_host_srv_diff_host_rate","dst_host_serror_rate","dst_host_srv_serror_rate", "dst_host_rerror_rate","dst_host_srv_rerror_rate","attack", "last_flag"]

#### BASIC FEATURES OF EACH NETWORK CONNECTION VECTOR:

1) <b>Duration:</b>  Length of time duration of the connection  
2) <b>Protocol_type:</b> Protocol used in the connection  
3) <b>Service:</b> Destination network service used  
4) <b>Flag:</b> Status of the connection – Normal or Error 
5) <b>Src_bytes:</b> Number of data bytes transferred from source to destination in single connection  
6) <b>Dst_bytes:</b> Number of data bytes transferred from destination to source in single connection  
7) <b>Land:</b> if source and destination IP addresses and port numbers are equal then, this variable takes value 1 else 0  
8) <b>Wrong_fragment:</b> Total number of wrong fragments in this connection  
9) <b>Urgent:</b> Number of urgent packets in this connection. Urgent packets are packets with the urgent bit activated

#### CONTENT RELATED FEATURES OF EACH NETWORK CONNECTION VECTOR:

10) <b>Hot:</b> Number of "hot" indicators in the content such as: entering a system directory, creating programs and executing programs 
11) <b>Num_failed _logins:</b> Count of failed login attempts  
12) <b>Logged_in Login Status:</b> 1 if successfully logged in; 0 otherwise  
13) <b>Num_compromised:</b> Number of "compromised" conditions  
14) <b>Root_shell:</b> 1 if root shell is obtained; 0 otherwise  
15) <b>Su_attempted:</b> 1 if "su root" command attempted or used; 0 otherwise  
16) <b>Num_root:</b> Number of "root" accesses or number of operations performed as a root in the connection 
17) <b>Num_file_creations:</b> Number of file creation operations in the connection  
18) <b>Num_shells:</b> Number of shell prompts  
19) <b>Num_access_files:</b> Number of operations on access control files  
20) <b>Num_outbound_cmds:</b> Number of outbound commands in an ftp session  
21) <b>Is_hot_login:</b> 1 if the login belongs to the "hot" list i.e., root or admin; else 0  
22) <b>Is_guest_login:</b> 1 if the login is a "guest" login; 0 otherwise 

#### TIME RELATED TRAFFIC FEATURES OF EACH NETWORK CONNECTION VECTOR:

23) <b>Count:</b> Number of connections to the same destination host as the current connection in the past two seconds 
24) <b>Srv_count:</b> Number of connections to the same service (port number) as the current connection in the past two seconds  
25) <b>Serror_rate:</b> The percentage of connections that have activated the flag (4) s0, s1, s2 or s3, among the connections aggregated in count (23)  
26) <b>Srv_serror_rate:</b> The percentage of connections that have activated the flag (4) s0, s1, s2 or s3, among the connections aggregated in srv_count (24)  
27) <b>Rerror_rate:</b> The percentage of connections that have activated the flag (4) REJ, among the connections aggregated in count (23)  
28) <b>Srv_rerror_rate:</b> The percentage of connections that have activated the flag (4) REJ, among the connections aggregated in srv_count (24)  
29) <b>Same_srv_rate:</b> The percentage of connections that were to the same service, among the connections aggregated in count (23)  
30) <b>Diff_srv_rate:</b> The percentage of connections that were to different services, among the connections aggregated in count (23)
31) <b>_diff_host_ rate:</b> percentage of connections that were to different destination machines among the connections aggregated in srv_count (24) 

####  HOST BASED TRAFFIC FEATURES IN A NETWORK CONNECTION VECTOR:

32) <b>Dst_host_count:</b> Number of connections having the same destination host IP address  
33) <b>Dst_host_srv_ count:</b> Number of connections having the same port number  
34) <b>Dst_host_same _srv_rate:</b> The percentage of connections that were to the same service, among the connections aggregated in dst_host_count (32)  
35) <b>Dst_host_diff_ srv_rate:</b> The percentage of connections that were to different services, among the connections aggregated in dst_host_count (32)  
36) <b>Dst_host_same _src_port_rate:</b> The percentage of connections that were to the same source port, among the connections aggregated in dst_host_srv_c ount (33)  
37) <b>Dst_host_srv_ diff_host_rate:</b> The percentage of connections that were to different destination machines, among the connections aggregated in dst_host_srv_count (33) 
38) <b>Dst_host_serro r_rate:</b> The percentage of connections that have activated the flag (4) s0, s1, s2 or s3, among the connections aggregated in dst_host_count (32)  
39) <b>Dst_host_srv_s error_rate:</b> The percent of connections that have activated the flag (4) s0, s1, s2 or s3, among the connections aggregated in dst_host_srv_c ount (33)  
40) <b>Dst_host_rerro r_rate:</b> The percentage of connections that have activated the flag (4) REJ, among the connections aggregated in dst_host_count (32)  
41) <b>Dst_host_srv_r error_rate:</b> The percentage of connections that have activated the flag (4) REJ, among the connections aggregated in dst_host_srv_c ount (33) 

#### Type Features:

<b>Nominal:</b>  Protocol_type(2), Service(3), Flag(4) 
 
<b>Binary:</b> Land(7), logged_in(12), root_shell(14), su_attempted(15), is_host_login(21),, is_guest_login(22) 
 
<b>Numeric:</b> Duration(1), src_bytes(5), dst_bytes(6), wrong_fragment(8), urgent(9), hot(10), num_failed_logins(11), num_compromised(13), num_root(16), num_file_creations(17), num_shells(18), num_access_files(19), num_outbound_cmds(20), count(23), srv_count(24), error_rate(25), srv_serror_rate(26), rerror_rate(27),srv_rerror_rate(28), same_srv_rate(29),diff_srv_rate(30), srv_diff_host_rate(31), dst_host_count(32), dst_host_srv_count(33), dst_host_same_srv_rate(34), dst_host_diff_srv_rate(35), dst_host_same_src_port_rate(36), dst_host_srv_diff_host_rate(37), dst_host_serror_rate(38), dst_host_srv_serror_rate(39), dst_host_rerror_rate(40), dst_host_srv_rerror_rate(41) 

### Attack Class : Attack Type
              
1) DoS       : Back, Land, Neptune, Pod, Smurf,Teardrop,Apache2, Udpstorm, Processtable, Worm (10) 

2) Probe     : Satan, Ipsweep, Nmap, Portsweep, Mscan, Saint  (6) 

3) R2L       : Guess_Password, Ftp_write, Imap, Phf, Multihop, Warezmaster, Warezclient, Spy, Xlock, Xsnoop, Snmpguess, Snmpgetattack, Httptunnel, Sendmail, Named (16)
 
4) U2R       : Buffer_overflow, Loadmodule, Rootkit, Perl, Sqlattack, Xterm, Ps (7) 

### ATTACK CLASS: 

1. <b>DOS:</b> Denial of service is an attack category, which depletes the victim‟s resources thereby making it unable to handle legitimate requests – e.g. syn flooding. Relevant features: “source bytes” and “percentage of packets with errors”  
2. <b>Probing:</b> Surveillance and other probing attack‟s objective is to gain information about the remote victim e.g. port scanning. Relevant features: “duration of connection” and “source bytes”  
3. <b>U2R:</b> unauthorized access to local super user (root) privileges is an attack type, by which an attacker uses a normal account to login into a victim system and tries to gain root/administrator privileges by exploiting some vulnerability in the victim e.g. buffer overflow attacks. Relevant features: “number of file creations” and “number of shell prompts invoked,” 
4. <b>R2L:</b> unauthorized access from a remote machine, the attacker intrudes into a remote machine and gains local access of the victim machine. E.g. password guessing Relevant features: Network level features – “duration of connection” and “service requested” and host level features - “number of failed login attempts” 

### How to Use

Just follow 3 simple steps :

1. Go to project website link https://nids-api.herokuapp.com/ .<br>

2. Fill the form as shown below :<br><br>

![](https://github.com/vicky60629/Network-Intrusion-Detection-System/blob/master/results/2020-06-15%2015_28_16-Window.png)<br>
![](https://github.com/vicky60629/Network-Intrusion-Detection-System/blob/master/results/2020-06-15%2015_29_02-Window.png)<br>

3. Then Click on Predict and you get the predicted attack class .<br><br>

![](https://github.com/vicky60629/Network-Intrusion-Detection-System/blob/master/results/2020-06-15%2015_30_02-Window.png)<br>

**If you face any problem :** email me at *vg60629@gmail.com*

### LICENSE

[MIT License](https://github.com/vicky60629/Network-Intrusion-Detection-System/blob/master/LICENSE)

Copyright (c) 2020 Vicky Gupta

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
