# Voyager && ChampSim

包含Voayger和ChampSim两个目录，其中Voyager用于训练模型，ChampSim用于对训练得到的模型进行模拟

## 数据集

复现论文所需数据集在该路径下 `https://utexas.app.box.com/s/2k54kp8zvrqdfaa8cdhfquvcxwh7yn85`

## 训练模型

训练包括在线训练和离线训练，论文中的展示结果为在线训练

### 在线训练

进入到voyager目录下，运行online.py在线训练模型，使用的配置文件为seq_multi.yaml

```
python online.py  --benchmark 473.astar-s0.txt.xz  --config configs/seq_multi.yaml --model-path ./models/astar_model --print-every 100 --tb-dir ./logs/astar   --prefetch-file   ./logs/astar_online_prefetch.txt
```

> --benchmark       指定trace文件
>
> --config               指定配置文件
>
> --model-path       指定模型存放路径
>
> --print-every        打印进度信息
>
>  --tb-dir                TensorBoard日志目录
>
> --prefetch-file      预取结果输出文件

训练完成后得到预取文件，将预取文件拷贝到ChampSim目录下

### 离线训练

训练模型

```
python train.py  --benchmark 473.astar-s0.txt.xz  --config configs/base.yaml --model-path ./models/astar_model --print-every 100 --tb-dir ./logs/astar 
```

生成预取文件

```
python generate.py --benchmark 473.astar-s0.txt.xz --config configs/base.yaml --model-path ./models/astar_model --prefetch-file ./logs/astar_prefetch_test.txt --print-every 100 --tb-dir ./logs/astar
```

## 模拟测试

进入到ChampSim目录下

### 构建

- 构建模拟器

```
./ml_prefetch_sim.py build
```

### 运行

- 只运行ChampSim的baseline，用于获取基准性能数据。

```
./ml_prefetch_sim.py run path_to_champsim_trace_here
```

- 同时运行baseline以及自定义预取器，用于对比性能

```
./ml_prefetch_sim.py run path_to_champsim_trace_here --prefetch path_to_prefetcher_file
```

- 只运行baseline，不运行预取器

```
./ml_prefetch_sim.py run path_to_trace_here --prefetch path_to_prefetcher_file --no-base
```

### 评估

- 评估结果

```
./ml_prefetch_sim.py eval
```

