**Study 용 예제 문서**<br>
### Network Configuration Command Option
| Option | Description |
|--|--|
| -d, -driver="bridge" | set driver|
| -ip-range=[] | allocate range |
| -subnet=[] | Subnet mask |


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

### Networking Connect to Container.

We can run Docker for example, which pull tomcat image if not found tomcat image.

```shell
docker run -it --net=myNetwork tomcat

Unable to find image 'tomcat:latest' locally
latest: Pulling from library/tomcat
cc1a78bfd46b: Pull complete
6861473222a6: Pull complete
7e0b9c3b5ae0: Pull complete
ae14ee39877a: Pull complete
8085c1b536f0: Pull complete
6e1431e84c0c: Pull complete
ca0e3df5a1fd: Pull complete
d2cb611ced6c: Pull complete
268dc3e43e66: Pull complete
79a7e8d254c7: Pull complete
5c848af92738: Pull complete
789b92e37607: Pull complete
Digest: sha256:a01c3ad30a211e742dabd74ff722374ab25c27b8d6162b210572a915305f1246
Status: Downloaded newer image for tomcat:latest
Using CATALINA_BASE:   /usr/local/tomcat
Using CATALINA_HOME:   /usr/local/tomcat
Using CATALINA_TMPDIR: /usr/local/tomcat/temp
Using JRE_HOME:        /docker-java-home/jre
Using CLASSPATH:       /usr/local/tomcat/bin/bootstrap.jar:/usr/local/tomcat/bin/tomcat-juli.jar
01-Jun-2018 07:31:31.246 INFO [main] org.apache.catalina.startup.VersionLoggerListener.log Server version:        Apache Tomcat/8.5.31
01-Jun-2018 07:31:31.248 INFO [main] org.apache.catalina.startup.VersionLoggerListener.log Server built:          Apr 27 2018 20:24:25 UTC
01-Jun-2018 07:31:31.249 INFO [main] org.apache.catalina.startup.VersionLoggerListener.log Server number:         8.5.31.0
01-Jun-2018 07:31:31.250 INFO [main] org.apache.catalina.startup.VersionLoggerListener.log OS Name:               Linux
01-Jun-2018 07:31:31.251 INFO [main] org.apache.catalina.startup.VersionLoggerListener.log OS Version:            4.4.0-1060-aws
01-Jun-2018 07:31:31.252 INFO [main] org.apache.catalina.startup.VersionLoggerListener.log Architecture:          amd64
01-Jun-2018 07:31:31.252 INFO [main] org.apache.catalina.startup.VersionLoggerListener.log Java Home:             /usr/lib/jvm/java-8-openjdk-amd64/jre
01-Jun-2018 07:31:31.254 INFO [main] org.apache.catalina.startup.VersionLoggerListener.log JVM Version:           1.8.0_171-8u171-b11-1~deb9u1-b11
01-Jun-2018 07:31:31.254 INFO [main] org.apache.catalina.startup.VersionLoggerListener.log JVM Vendor:            Oracle Corporation
01-Jun-2018 07:31:31.255 INFO [main] org.apache.catalina.startup.VersionLoggerListener.log CATALINA_BASE:         /usr/local/tomcat
01-Jun-2018 07:31:31.255 INFO [main] org.apache.catalina.startup.VersionLoggerListener.log CATALINA_HOME:         /usr/local/tomcat

```
