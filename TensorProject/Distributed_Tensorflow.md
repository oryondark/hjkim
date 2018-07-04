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
