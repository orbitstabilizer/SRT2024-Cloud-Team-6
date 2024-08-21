# Low Load

```
hasan@hasan-GP66-Leopard-10UE:~/Desktop/cloud1$ ab -n 100 -c 1 http://192.168.0.25:8080/time
This is ApacheBench, Version 2.3 <$Revision: 1879490 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 192.168.0.25 (be patient).....done


Server Software:        SimpleHTTP/0.6
Server Hostname:        192.168.0.25
Server Port:            8080

Document Path:          /time
Document Length:        27 bytes

Concurrency Level:      1
Time taken for tests:   0.059 seconds
Complete requests:      100
Failed requests:        79
   (Connect: 0, Receive: 0, Length: 79, Exceptions: 0)
Total transferred:      14775 bytes
HTML transferred:       2775 bytes
Requests per second:    1698.43 [#/sec] (mean)
Time per request:       0.589 [ms] (mean)
Time per request:       0.589 [ms] (mean, across all concurrent requests)
Transfer rate:          245.06 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.2      0       2
Processing:     0    0   0.3      0       2
Waiting:        0    0   0.2      0       1
Total:          0    1   0.4      0       2
ERROR: The median and mean for the total time are more than twice the standard
       deviation apart. These results are NOT reliable.

Percentage of the requests served within a certain time (ms)
  50%      0
  66%      0
  75%      0
  80%      0
  90%      1
  95%      2
  98%      2
  99%      2
 100%      2 (longest request)

```

# Medium Load

```
hasan@hasan-GP66-Leopard-10UE:~/Desktop/cloud1$ ab -n 1000 -c 10 http://192.168.0.25:8080/time
This is ApacheBench, Version 2.3 <$Revision: 1879490 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 192.168.0.25 (be patient)
Completed 100 requests
Completed 200 requests
Completed 300 requests
Completed 400 requests
Completed 500 requests
Completed 600 requests
Completed 700 requests
Completed 800 requests
Completed 900 requests
Completed 1000 requests
Finished 1000 requests


Server Software:        SimpleHTTP/0.6
Server Hostname:        192.168.0.25
Server Port:            8080

Document Path:          /time
Document Length:        28 bytes

Concurrency Level:      10
Time taken for tests:   0.828 seconds
Complete requests:      1000
Failed requests:        255
   (Connect: 0, Receive: 0, Length: 255, Exceptions: 0)
Total transferred:      147715 bytes
HTML transferred:       27715 bytes
Requests per second:    1207.71 [#/sec] (mean)
Time per request:       8.280 [ms] (mean)
Time per request:       0.828 [ms] (mean, across all concurrent requests)
Transfer rate:          174.22 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       1
Processing:     1    5  39.6      2     827
Waiting:        0    5  39.6      2     827
Total:          1    5  39.6      3     827

Percentage of the requests served within a certain time (ms)
  50%      3
  66%      3
  75%      3
  80%      3
  90%      3
  95%      3
  98%      3
  99%      3
 100%    827 (longest request)
```

# High Load

```
hasan@hasan-GP66-Leopard-10UE:~/Desktop/cloud1$ ab -n 2000 -c 20 http://192.168.0.25:8080/time
This is ApacheBench, Version 2.3 <$Revision: 1879490 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 192.168.0.25 (be patient)
Completed 200 requests
Completed 400 requests
Completed 600 requests
Completed 800 requests
Completed 1000 requests
Completed 1200 requests
Completed 1400 requests
Completed 1600 requests
Completed 1800 requests
Completed 2000 requests
Finished 2000 requests


Server Software:        SimpleHTTP/0.6
Server Hostname:        192.168.0.25
Server Port:            8080

Document Path:          /time
Document Length:        27 bytes

Concurrency Level:      20
Time taken for tests:   0.826 seconds
Complete requests:      2000
Failed requests:        1580
   (Connect: 0, Receive: 0, Length: 1580, Exceptions: 0)
Total transferred:      295491 bytes
HTML transferred:       55491 bytes
Requests per second:    2419.88 [#/sec] (mean)
Time per request:       8.265 [ms] (mean)
Time per request:       0.413 [ms] (mean, across all concurrent requests)
Transfer rate:          349.15 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.1      0       1
Processing:     0    3  31.3      2     825
Waiting:        0    3  31.3      1     825
Total:          0    3  31.3      2     826

Percentage of the requests served within a certain time (ms)
  50%      2
  66%      2
  75%      2
  80%      2
  90%      2
  95%      2
  98%      2
  99%      3
 100%    826 (longest request)
```
