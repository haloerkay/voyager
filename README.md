# Voyager && ChampSim

包含Voayger和ChampSim两个目录，其中Voyager用于训练模型，ChampSim用于对模型生成的预取文件进行模拟测试

## 数据集

复现论文所需数据集在该路径下 https://utexas.app.box.com/s/2k54kp8zvrqdfaa8cdhfquvcxwh7yn85

- ./LoadTraces，用于训练模型，获得预取文件

- ./ChampSimTraces，用于模拟测试

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

训练完成后得到预取文件，用于后续的模拟步骤

### 离线训练

训练模型

```
python train.py  --benchmark 473.astar-s0.txt.xz  --config configs/base.yaml --model-path ./models/astar_model --print-every 100 --tb-dir ./logs/astar 
```

生成预取文件

```
python generate.py --benchmark 473.astar-s0.txt.xz --config configs/base.yaml --model-path ./models/astar_model --prefetch-file ./logs/astar_prefetch_test.txt --print-every 100 --tb-dir ./logs/astar
```

## 模拟步骤

### 下载Traces

在地址(https://utexas.box.com/s/2k54kp8zvrqdfaa8cdhfquvcxwh7yn85).  下载trace并解压为txt文件到 需要将473.astar-s0 训练trace下载到trace/train中

### 构建

编译C++代码，构建模拟器

```
./ml_prefetch_sim.py build
```

### 运行

运行下面代码生成无预取器的基线结果

```
./ml_prefetch_sim.py run path_to_champsim_trace_here
```

path_to_champsim_trace_here 为测试trace的xz文件路径
运行下面代码将预取结果在模拟平台模拟运行

```
./ml_prefetch_sim.py run path_to_trace_here --prefetch path_to_prefetcher_file --no-base
```

path_to_trace_here 为测试trace的xz文件路径  path_to_prefetcher_file 为预取文件路径，目前Voyager，ISB，BO，STMS预取器生成的文件都在./predict下
最后的模拟结果保存在473.astar-s0.trace.gz-from_file.txt 中。
