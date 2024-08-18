# Week 1 - Part 1

## Files
```
.
├── README.md
├── Week_1.pdf
├── benchmark
│   ├── local_benchmark.txt
│   ├── multipass_benchmark.txt
│   └── remote_benchmark.txt
└── src
    └── server.py
```

### `src/server.py`
This is a simple HTTP server that serves the current time in seconds since the epoch
Server:
    Host: 127.0.0.1
    Port: 8080
Endpoint:
    GET /time

### `benchmark`
Contains apache benchmark results:
#### Local run
``` bash
# RAM:18GB, CPU: M3 Pro
python3 src/server.py &
ab -n 100 -c 5 127.0.0.1:8080/time > benchmark/local_benchmark.txt
```

#### VM run
``` bash
# <multipass> is a multipass ubuntu Ubuntu 24.04 LTS machine
#  RAM:1GB, CPU:1, disk:5GB
scp src/server.py <multipass>:~/
ssh <multipass> "python3 ~/server.py" &
ssh -NL 8080:127.0.0.1:8080 <multipass> &
ab -n 100 -c 5 127.0.0.1:8080/time > benchmark/multipass_benchmark.txt
```

#### Remote run
``` bash
# <remote> is a macbook pro machine
# RAM:8GB, CPU: M3
scp src/server.py <remote>:~/
ssh <remote> "python3 ~/server.py" &
ssh -NL 8080:127.0.0.1:8080 <remote> &
ab -n 100 -c 5 127.0.0.1:8080/time > benchmark/remote_benchmark.txt
```
#### Docker Container run
``` bash
# assuming you have Docker engine installed
docker build -t week-1-server . # build the docker image
# crate an instance of week-1-server image and bind service port
docker run -d -p 8080:8080 --name pytime week-1-server # -d for detach
docker start pytime # start the instance
ab -n 100 -c 5 127.0.0.1:8080/time > benchmark/docker_benchmark.txt
```
