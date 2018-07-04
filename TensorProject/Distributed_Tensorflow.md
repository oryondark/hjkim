API usage for Distributed Tensorflow

1. basic run with GPUOptions <br>
```python
g_opt = tf.GPUOptions(per_process_gpu_memory_fraction=0.5)
config = tf.ConfigProto(gpu_options=g_opt)
sess = tf.Session(config=config)
sess.run()
```
