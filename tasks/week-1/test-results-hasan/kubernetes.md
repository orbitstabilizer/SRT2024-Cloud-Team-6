# Low Load

```
hasan@hasan-GP66-Leopard-10UE:~/Desktop/cloud1$ ab -n 100 -c 10 http://127.0.0.1:8080/time
This is ApacheBench, Version 2.3 <$Revision: 1879490 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 127.0.0.1 (be patient).....done


Server Software:        SimpleHTTP/0.6
Server Hostname:        127.0.0.1
Server Port:            8080

Document Path:          /time
Document Length:        28 bytes

Concurrency Level:      10
Time taken for tests:   14.273 seconds
Complete requests:      100
Failed requests:        24
   (Connect: 0, Receive: 0, Length: 24, Exceptions: 0)
Total transferred:      14773 bytes
HTML transferred:       2773 bytes
Requests per second:    7.01 [#/sec] (mean)
Time per request:       1427.313 [ms] (mean)
Time per request:       142.731 [ms] (mean, across all concurrent requests)
Transfer rate:          1.01 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.1      0       0
Processing:  1219 1373 268.1   1294    2319
Waiting:      212  340 265.4    236    1256
Total:       1219 1374 268.1   1294    2319

Percentage of the requests served within a certain time (ms)
  50%   1294
  66%   1331
  75%   1354
  80%   1403
  90%   1535
  95%   2198
  98%   2319
  99%   2319
 100%   2319 (longest request)
```

# Medium Load

```
hasan@hasan-GP66-Leopard-10UE:~/Desktop/cloud1$ ab -n 1000 -c 10 http://127.0.0.1:8080/time
This is ApacheBench, Version 2.3 <$Revision: 1879490 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 127.0.0.1 (be patient)
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
Server Hostname:        127.0.0.1
Server Port:            8080

Document Path:          /time
Document Length:        27 bytes

Concurrency Level:      10
Time taken for tests:   130.933 seconds
Complete requests:      1000
Failed requests:        769
   (Connect: 0, Receive: 0, Length: 769, Exceptions: 0)
Total transferred:      147721 bytes
HTML transferred:       27721 bytes
Requests per second:    7.64 [#/sec] (mean)
Time per request:       1309.331 [ms] (mean)
Time per request:       130.933 [ms] (mean, across all concurrent requests)
Transfer rate:          1.10 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.2      0       2
Processing:  1207 1299 182.9   1241    2378
Waiting:      205  283 183.2    233    1462
Total:       1207 1299 182.9   1241    2378

Percentage of the requests served within a certain time (ms)
  50%   1241
  66%   1274
  75%   1301
  80%   1317
  90%   1344
  95%   1526
  98%   2220
  99%   2290
 100%   2378 (longest request)
```
