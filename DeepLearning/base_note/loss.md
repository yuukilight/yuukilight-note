## 🧠 Loss
### Cross Entropy

熵 (Entropy) 起源于物理学，用来度量热力学系统的无序程度。

熵越高，越混乱，信息越多，越难以预测。

用概率进行表示，概率越小，越混乱，熵越高。可以用对数很好的进行定义。

### InfoNCE Loss
InfoNCE Loss 是目前最有效且通用的对比学习损失，适用于点云与语言表示对齐。

InfoNCE(Noise Contrastive Estimation), 和 Cross Entropy 计算相比，相当于把类别得分替换为了相似度。因此可以直接使用深度学习框架中的 Cross Entropy Loss 模块（例如torch 中的 CrossEntropyLoss）计算。

NCE Loss 与 InfoNCE Loss

### Triplet Loss

提出主要出自[Deep Face Recognition](https://www.robots.ox.ac.uk/~vgg/publications/2015/Parkhi15/parkhi15.pdf)和[FaceNet](https://arxiv.org/abs/1503.03832)

提出背景: 人脸识别中，把不同的人脸区分当成一个多分类任务处理不合理。因为人脸的种类可以认为有无穷多种，是不可能完全划分的。一种合理的想法是，减小类内距离（intra-class distance）和增大类间距离(inter-class distance)。

(ps:
    类内距离：同一张脸的不同表情
    类间距离：不同的脸
)

因此得到了如下损失函数:
$Loss_{triplet} = max(0, distance(a, p) + margin - distance(a, n))$
anchor作为基准特征向量，postive 为正样本，negtive 为负样本。

也就是当$distance(a, p) + margin > distance(a, n)$ 时，需要减小 distance(a, p) 并增大 distance(a, n)

**a, p, n 的选取**
分为离线和在线，一般选择在线选取的方式

**缺点**
没有考虑具体的数据分布情况，训练时选取的大部分(a, n, p) 三元组都是没有意义的。

### Center Loss
[paper](https://ydwen.github.io/papers/WenECCV16.pdf)and[code](https://github.com/ydwen/caffe-face)
Center Loss 的主要思想是尽可能的缩小类内的距离。在一个 mini batch 种使用如下公式：
$$L_C = \frac{1}{2} \sum_{1}^{m} \lVert x_i - c_{y_i}\rVert ^2$$
其中$x_i$ 是一个样本，$c_{y_i}$ 是类中心。只有当$x_i$ 和 $c_{y_i}$ 同属于一个类才会更新这个Loss。

### Angular Margin Loss
Angular Margin Loss 是如下一系列 Loss 函数的统称。
> 1. Sphereface:[paper](https://arxiv.org/abs/1704.08063) and [code](https://github.com/wy1iu/sphereface)
> 2. Large margin softmax: [paper](https://arxiv.org/abs/1612.02295) and [code](https://github.com/wy1iu/LargeMargin_Softmax_Loss)
> 3. Additive margin softmax: [paper](https://arxiv.org/abs/1801.05599) and [code](https://github.com/happynear/AMSoftmax)
> 4. CosFace: [paper](https://arxiv.org/abs/1801.09414)
> 5. ArcFace/InsightFace: [paper](https://arxiv.org/abs/1801.07698) and [code](https://github.com/deepinsight/insightface)
> 6. NormFace: [paper](https://arxiv.org/abs/1704.06369) and [code](https://github.com/happynear/NormFace)
> 7. L2-Softmax: [paper](https://arxiv.org/abs/1703.09507)
> 8. von Mises-Fisher Mixture Model: [paper](https://arxiv.org/abs/1706.04264)
> 9. COCO loss: [paper](https://arxiv.org/pdf/1710.00870.pdf) and [code](https://github.com/sciencefans/coco_loss)
> 10. Angular Triplet Loss: [code](https://github.com/KaleidoZhouYN/Angular-Triplet-Loss)

经过上面的工作，最终发展到效果最好的采用 Cosine 距离以及角度 Margin 的思想。