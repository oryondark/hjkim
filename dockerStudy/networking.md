**Study 용 예제 문서**<br>
### Network Configuration Command Option
| Option | Description |
|--|--|
| -d, -driver="bridge" | set driver|
| -aux-address=map[] | 


### Configure for network base<br>
```bash
  $ docker network create myNetwork
  687c871657046f3263f852ec796ad45488a940cd64e6b5c9a96b64d869b7b208
  
  $ docker network inspect myNetwork
  [
    {
        "Name": "myNetwork",
        "Id": "687c871657046f3263f852ec796ad45488a940cd64e6b5c9a96b64d869b7b208"                                                                                        ,
        "Created": "2018-06-01T04:04:28.344011184Z",
        "Scope": "local",
        "Driver": "bridge",
        "EnableIPv6": false,
        "IPAM": {
            "Driver": "default",
            "Options": {},
            "Config": [
                {
                    "Subnet": "172.18.0.0/16",
                    "Gateway": "172.18.0.1"
                }
            ]
        },
        "Internal": false,
        "Attachable": false,
        "Ingress": false,
        "ConfigFrom": {
            "Network": ""
        },
        "ConfigOnly": false,
        "Containers": {},
        "Options": {},
        "Labels": {}
    }
]
```

