[toc]

## PointContrast: Unsupervised Pre-training for 3D Point Cloud Understanding  
**📌 Tags:** `unsupervised-learning` `point-cloud` `3D` `pretraining`  
**📚 Venue:** ECCV 2020
**🔗 PDF:** [arXiv link](https://arxiv.org/abs/2007.10985)

## Towards Large-scale 3D Representation Learningwith Multi-dataset Point Prompt Training
**📌 Tags:** `multi-dataset` `point-cloud` `3D` `pretraining`  
**📚 Venue:** CVPR 2024
**🔗 PDF:** [arXiv link](https://arxiv.org/abs/2308.09718)

提出 Promt-driven Normalization, 为数据集编码一组特征向量，并通过该特征向量计算一组$\beta$, $\gamma$参数来对网络结构backbone 中的 normalize 后的特征向量进行缩放和位移。以让网络结构适应不同的数据集。

提出 Language-guided Categorical Alignment, 利用CLIP将标签语义信息进行编码，让模型预测的结果去逼近对应标签的特征向量以适应多个数据集标签不同的问题。

## OpenAnnotate3D: Open-Vocabulary Auto-Labeling System for Multi-modal 3D Data
**📌 Tags:** `LLMs` `point-cloud` `3D` `VLMs`
**🔗 PDF:** [arXiv link](https://arxiv.org/pdf/2310.13398)
使用 gpt 的接口调用大语言模型，根据用户的输入迭代生成详细的标签语义信息。然后通过 Grounding DINO 和 SAM 模型在 2D 图上生成 MASK，然后映射到 3D 点云中。(Multi-modal Spatial Alignment 和 Spatio temporal fusion & correction)

## Segment Anything in 3D with Radiance Fields
**📌 Tags:** `3D Segmentation`, `Radiance Fields`, `3D Gaussian Splatting`, `Segment Anything Model`
**🔗 PDF:** [arXiv link](https://arxiv.org/pdf/2304.12308)

## SAM3D: Segment Anything in 3D Scenes

## A Unified Framework for 3D Scene Understanding
**📌 Tags:** `Seg3D` `Interactive Seg` ` Distillation` `Contrastive`
**🔗 PDF:** [arXiv link](https://arxiv.org/abs/2407.03263)
建立了一种统一的框架，能够同时支持 Panoptic Seg, Semantic Seg, Instance Seg, Interactive Seg, Referring Seg, OV Seg.

