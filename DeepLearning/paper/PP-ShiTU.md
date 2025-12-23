# PP-ShiTu: A Practical Lightweight Image Recognition System

一个实用轻量级通用图像识别系统。由主题检测、特征提取、向量检索三个模块构成。

[toc]

## 0. 前置知识
### 0.1. PP-LCNetv1
[官方文档](https://github.com/PaddlePaddle/PaddleClas/blob/release/2.6/docs/zh_CN/models/ImageNet1k/PP-LCNet.md)

**激活函数**
使用 H-Swish, 该函数去除了指数运算，速度更快，网络精度几乎不受影响。
经过实验 H-Swish 在轻量级网络有优异的表现。

Swish 对于负值也有一定程度的梯度。缓解梯度消息的问题。非单调性。正负之间过度平滑。
但是计算复杂。sigmoid 函数存在指数运算。

h-Swish 对 Swish 函数进行了拟合，同时移除了指数函数的计算，提高了计算效率。

**SE模块**

SE模块的使用会增加模型的推理时间。为了尽可能提高效果的同时，减少推理时间的增长。

实验发现SE模块插入的位置越靠后，效果越好。


**更大的卷积核**

一定范围内大的卷积核可以提升模型的性能，但是大的卷积核会影响推理，特别是大小卷积核混合使用的时候。

作者实验大卷积核的位置，发现和SE模块类似，放在靠后的位置作用更明显。

**GAP后使用更大的 1x1 卷积层**

轻量级模型的通道数更小，GAP层后直接接分类成，会导致分类用的特征少，没有进一步的融合和加工。

添加更大的 1x1 卷积层(输出通道大于输入通道)让特征融合和加工后再分类。

**蒸馏**
使用了SSLD蒸馏，[Paddle 蒸馏相关介绍](https://github.com/PaddlePaddle/PaddleClas/blob/release/2.6/docs/zh_CN/training/advanced/knowledge_distillation.md)

**其它**

文档中给出不同规模模型，调整的是通道数。

### 0.2 PP-LCNetv2
**$\star$Rep策略**
- 计算库（如CuDNN,Intel MKL）和硬件针对3x3卷积有深度的优化。--> 尽量使用统一的 3x3 卷积结构。
- 网络的多分支结构往往有更好的性能，但是显存占用高，推理速度慢。 --> 训练阶段多分支，推理时采用结构重参数化思想融合成单路结构。

kernel size 统一成最大的，然后合并。

***为什么Conv+Bn, 训练和推理用不同的处理方式是可行的***
BN层中的均值$\mu$和方差$\sigma$, 在训练阶段为了更快的收敛是计算的当前batch的，是不固定的。同时会计算一组全局$\mu_{all}$ 和 $\sigma_{all}$。

推理阶段使用的$\mu_{all}$ 和 $\sigma_{all}$以及固定下来了，这时可以提前计算好不同卷积分支的参数，然后统一成一个卷积操作的单路结构。

**PW卷积**
深度可分离卷积通常由一层 Depthwise 和 一层 Pointwise 组成。
PP=LCNetv2 中添加了一层 Pointwise, 先将通道缩小再放大。

实验证明该操作能显著提高模型性能。

为了平衡对模型效率带来的影响，仅在Stage4中使用。

**Shortcut**
shortcut 的 element-wise 加法操作会影响模型的速度。

实验发现残差结构并非一定会带来提升，同样的只在最后一个stage中使用。

**激活函数**
部分推理平台对于Hard-Swish的效率优化不理想，最后使用更通用的ReLu函数。

***一点启发***：不同的平台先做一些预实验，以激活函数为例，测试不同激活函数的运行效率。再以次进一步的确定模型。

## 主体检测
[官方文档](https://github.com/PaddlePaddle/PaddleClas/blob/release/2.6/docs/zh_CN/training/PP-ShiTu/mainbody_detection.md)
### 数据集
**使用到的数据集**
通用场景[Objects365](https://www.objects365.org/overview.html)
通用场景[COCO2017](https://cocodataset.org/)
动漫人脸检测[iCartoonFace](https://github.com/luxiangju-PersonAI/iCartoonFace)
Logo检测[LogoDet-3k](https://github.com/Wangjing1551/LogoDet-3K-Dataset)
商品检测[RPC](https://rpc-dataset.github.io/)

由于是主体检测，因此将所有标注框的类别都设置为前景(fore ground)。

**数据集的格式**

使用 coco 数据集的格式。所有标签的 category_id 修改为 1, 所有标签类别都映射到 foreground。

### 主体检测模型

使用 PicoDet 系列模型。轻量级，适用于移动端、CPU端。

**使用的优化算法**
- VFL+GFL
- 新的 PAN Neck 结构
- 余弦学习率策略
- Cyde-EMA
- ATSS及SimOTA标签分配策略

### 模型训练

**知识蒸馏**
1. 使用预训练好的模型
2. 使用模型自身

- $\star$可以作为软件训练的高级参数

## 特征提取
将输入的图片转化为固定维度的特征向量，用于后续的向量检索。
选择了自研的 [PPLCNetV2_base](https://github.com/PaddlePaddle/PaddleClas/blob/release/2.6/docs/zh_CN/models/ImageNet1k/PP-LCNetV2.md)
[PPLCNetV2_base_ShiTu 详细信息](https://github.com/PaddlePaddle/PaddleClas/blob/release/2.6/docs/zh_CN/training/PP-ShiTu/feature_extraction.md)

### 什么是一个好的特征？
此处的特征一般都是指特征向量
好的特征通常需要具备"相似度保持性"。即相似度高的图片对，其特征的相似度也高（特征空间距离近），相似度低的图片对，其特征的相似度也低（特征空间距离远）。

### 特征提取模型
为了图像识别任务的灵活定制，我们将整个网络分为 Backbone、 Neck、 Head 以及 Loss 部分。

**Backbone**
用于提取图像初步特征的骨干网络。
采用[PP-LCNetV2_base](https://github.com/PaddlePaddle/PaddleClas/blob/release/2.6/docs/zh_CN/models/ImageNet1k/PP-LCNetV2.md)

在 [PPLCNet_v1](https://github.com/PaddlePaddle/PaddleClas/blob/release/2.6/docs/zh_CN/models/ImageNet1k/PP-LCNet.md) 基础上添加了 Rep 策略，PW卷积，Shortcut，激活函数改进，SE模块改进等

实验过程进一步改进，去掉了结尾的 ReLu 和 FC， 将最后的 stage(RepDepthwiseSeparable) 的 stride 改为1。

**Neck**
用以特征增强及特征维度变换。可以是简单的 FC Layer。

采用了[BN_Neck](https://github.com/PaddlePaddle/PaddleClas/blob/release/2.6/ppcls/arch/gears/bnneck.py)
对 Backbone 抽取得到的特征的每个维度进行标准化操作，减少了同时优化度量学习损失函数和分类损失函数的难度，加快收敛速度。

**Head**
用来将 Neck 输出的 feature 转化为 logits, 让模型在训练阶段能以分类任务的形式进行训练。

Head 部分选用 [FC Layer](https://github.com/PaddlePaddle/PaddleClas/blob/release/2.6/ppcls/arch/gears/fc.py)，使用分类头将 feature 转换成 logits 供后续计算分类损失。

**Loss**
指定所使用的 Loss 函数。PP-ShiTu将 Loss 设计为组合 loss 的形式，可以方便地将 Classification Loss 和 Metric learning Loss 组合在一起。

Loss 部分选用 [Cross entropy loss](https://github.com/PaddlePaddle/PaddleClas/blob/release/2.6/ppcls/loss/celoss.py) 和 
[TripletAngularMarginLoss](https://github.com/PaddlePaddle/PaddleClas/blob/release/2.6/ppcls/loss/tripletangularmarginloss.py)，在训练时以分类损失和基于角度的三元组损失来指导网络进行优化。我们基于原始的 TripletLoss (困难三元组损失)进行了改进，将优化目标从 L2 欧几里得空间更换成余弦空间，并加入了 anchor 与 positive/negtive 之间的硬性距离约束，让训练与测试的目标更加接近，提升模型的泛化能力。详细的配置文件见 [GeneralRecognitionV2_PPLCNetV2_base.yaml](https://github.com/PaddlePaddle/PaddleClas/blob/release/2.6/ppcls/configs/GeneralRecognitionV2/GeneralRecognitionV2_PPLCNetV2_base.yaml#L63-77)。

**Data Augmentation**
我们考虑到实际相机拍摄时目标主体可能出现一定的旋转而不一定能保持正立状态，因此我们在数据增强中加入了适当的[随机旋转增强](https://github.com/PaddlePaddle/PaddleClas/blob/release/2.6/ppcls/configs/GeneralRecognitionV2/GeneralRecognitionV2_PPLCNetV2_base.yaml#L117)，以提升模型在真实场景中的检索能力。

### DeepHash
使用的DSHSD

## 向量检索
使用 Faiss 向量检索库，对模型提取的特征向量建库和查询。
