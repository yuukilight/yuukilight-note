metric learning 也可以称为 distance metirc learning, 即度量学习。

metric-based methods (KNN, K-means)。

metric learning 可以和 metric-based methods 结合起来实现分类或聚类。
metric learning 效果好的情况下可以媲美很多很复杂的分类器。

# 简介
## 从 distance metric learning 的 distance 说起

距离与相似度。距离远=相似度低，距离近=相似度高。

往往我们认为距离近的样本之间，有更高的相似度，有更大的概率是属于同一类别。

### 度量距离的方式
**欧氏距离(Euclidean distance)**
只能处理维度相同的向量

两个向量在时间轴上有偏移，欧氏距离的效果会比较差。这个时候可以用DTW(Dynamic Time Warping) 距离替代。

**闵氏距离(Minkowski distance)**
即P阶距离，欧氏距离即2阶的闵氏距离，曼哈顿距离则是1阶的闵氏距离。

**马氏距离(Mahalanobis distance)**

其它还有诸如，余弦相似度，Hamming distance, KL散度等。

## 发展史
2002年，Eric Xing与Andrew Ng、Michael Jordan等人在NOPS上发表"Distance metric learning with application to clustering with side-information"。

## 学习到的是什么？
学习到一组空间变换的参数，让同一类别的样本距离更近，不同类别的样本距离更远。

## Metric Learning 的优势是什么？
增加新的类别后不需要重新定义网络模型结构，重新训练。

# Loss function



# Reference
- [1] [漫谈-Distance Metric Learning那些事儿](https://zhuanlan.zhihu.com/p/458114525)

1. 找对击球点，打到球
2. 步伐
3. 借助身体发力，减少肩膀发力
4. 网前手法