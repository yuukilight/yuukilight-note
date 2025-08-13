## 🧠 Loss
### Cross Entropy

熵 (Entropy) 起源于物理学，用来度量热力学系统的无序程度。

熵越高，越混乱，信息越多，越难以预测。

用概率进行表示，概率越小，越混乱，熵越高。可以用对数很好的进行定义。

### InfoNCE Loss
InfoNCE Loss 是目前最有效且通用的对比学习损失，适用于点云与语言表示对齐。

InfoNCE(Noise Contrastive Estimation), 和 Cross Entropy 计算相比，相当于把类别得分替换为了相似度。因此可以直接使用深度学习框架中的 Cross Entropy Loss 模块（例如torch 中的 CrossEntropyLoss）计算。

NCE Loss 与 InfoNCE Loss
