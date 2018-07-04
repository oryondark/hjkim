API usage for Distributed Tensorflow

1. basic run with GPUOptions <br>
```python
# fraction range 0 - 1
# fraction = 0.5 = 0 ~ 50%
g_opt = tf.GPUOptions(per_process_gpu_memory_fraction=0.5)
config = tf.ConfigProto(gpu_options=g_opt)
sess = tf.Session(config=config)
sess.run()
```

2. riseML platform for easy tensorflow scheduling<br>
https://riseml.com/ <br>

3. Distributed Tensorflow on Kubernetes
https://mengdong.github.io/2017/07/15/distributed-tensorflow-with-gpu-on-kubernetes-and-mapr/ 

