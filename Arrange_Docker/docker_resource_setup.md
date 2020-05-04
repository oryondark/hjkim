### Set up guide for docker
```shell
nvidia-docker run -it \
-m=1024m --memory-swap=0m \
--cpu-period=200000 --cpu-quota=100000 --cpuset-cpus=1,2 \
-p 10232:80 --name dockerwebbindingserver \
--mount type=bind,source=/mnt,target=/dockermnt \
nvidia/cuda:9.0-devel-ubuntu16.04 /bin/bash
```
### summary.
1. `-m` : allocate logical memory in physical memory size.
2. `--memory-swap`
3. `--cpu-period and --cpu-quota` : limitation of cpu usage. for example, ( quota / period = usage resource)
4. `--cpuset-cpus` : you can set you want to select cpu number.
5. `-p` : Network biding policy
6. `--mount` : `type` if bind, you should be wrote source directory such as `/mnt` and target directory(make directory) like `\dockermnt`
