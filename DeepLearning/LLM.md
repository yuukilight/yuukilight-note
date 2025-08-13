
## 发展
### 初代GPT
最初的NLP任务主要还处于 word2vec 和为不同的任务做定制化的深度学习模型的阶段。

最初的 GPT 原文标题 **Improving Language Understanding by Generative Pre-Training**, GPT 也就是指的 Generative Pre-Training.
进而引出文章想解决的问题，通过生成式预训练来提高模型对语言的理解能力，让模型获得强大的泛化性能。以及后续如何将这个模型迁移到各种下游任务。

提出了 pre-train + fine-tuning 的范式

### GPT2
GPT-2 原文标题为 Language Models are Unsupervised Multitask Learners，字面意思为语言模型是一种无监督多任务学习器。
这里的多任务是指模型从大规模数据中学到的能力能够直接在多个任务之间进行迁移，不需要而外提供特定任务的数据，因此引出了GPT-2的主要观点：zero-shot。

GPT1中会根据不同的任务类型，对输入的序列进行改造。但是在 zero-shot 的设定下无法这样做。

GPT2希望能够从规模足够大的语料库中学习到各种有监督的任务。因为语料库中本身就存在各种领悟和各个方向的任务（提问）。例如一些语料库中会提到将一种语言翻译成另一种语言。

增大了输入序列和模型的规模，并且为了减小模型层数增加带来的梯度消失和梯度爆炸的风险。做出了一些调整。

#### 与 GPT-1 的区别
整体来看，GPT-2 相比于 GPT-1 有如下几点区别：

1. 主推 zero-shot，而 GPT-1 为 pre-train + fine-tuning；
2. 训练数据规模更大，GPT-2 为 800w 文档 40G，GPT-1 为 5GB；
3. 模型大小，GPT-2 最大 15 亿参数，GPT-1为 1 亿参数；
4. 模型结构调整，层归一化和参数初始化方式；
5. 训练参数，batch_size 从 64 增加到 512，上文窗口大小从 512 增加到 1024，等等


### GPT3
GPT2具体的表现比较平庸，因此为了解决具体效果上的不足，提出了GPT3:Language Models are Few-Shot Learners。这里的 Few-shot 也不同于常规的用少量样本在下游任务上微调，因为这样大规模的模型只是微调成本也相当的高。

模型结构中引入了 sparse attention, 与传统的self-attention(dense attention) 的区别在于:
- dense attention：每个 token 之间两两计算 attention，复杂度 O(n²)
- sparse attention：每个 token 只与其他 token 的一个子集计算 attention，复杂度 O(n*logn)

即与相对距离小于k, 以及相对距离为 2k,3k,4k... 的token 进行计算。其余的token的注意力都设为0。

好处：
1. 减少计算复杂度
2. 局部紧密相关，远程稀疏相关

GPT-3 在下游任务的评估与预测时，提供了三种不同的方法：
- Zero-shot：仅使用当前任务的自然语言描述，不进行任何梯度更新；
- One-shot：当前任务的自然语言描述，加上一个简单的输入输出样例，不进行任何梯度更新；
- Few-shot：当前任务的自然语言描述，加上几个简单的输入输出样例，不进行任何梯度更新；

Few-shot 也称为 in-context learning。 与fine-tuning 不同。
1. fine-tuning 会对模型进行更新，in-context learning 不会。
2. in-context learning 需要的数据量（10~100）远远小于 fine-tuning 一般的数据量。

### InstructGPT
GPT-3 虽然在各大 NLP 任务以及文本生成的能力上令人惊艳，但是他仍然还是会生成一些带有偏见的，不真实的，有害的造成负面社会影响的信息，而且很多时候，他并不按人类喜欢的表达方式去说话。在这个背景下，OpenAI 提出了一个概念“Alignment”，意思是模型输出与人类真实意图对齐，符合人类偏好。因此，为了让模型输出与用户意图更加 “align”，就有了 InstructGPT 这个工作。

InstructGPT 相对于之前的 GPT 系列，有以下几点值得注意：

1. 解决 GPT-3 的输出与人类意图之间的 Align 问题；
2. 让具备丰富世界知识的大模型，学习“人类偏好”；
3. 标注人员明显感觉 InstructGPT 的输出比 GPT-3 的输出更好，更可靠；
4. InstructGPT 在真实性，丰富度上表现更好；
5. InstructGPT 对有害结果的生成控制的更好，但是对于“偏见”没有明显改善；
6. 基于指令微调后，在公开任务测试集上的表现仍然良好；
7. InstructGPT 有令人意外的泛化性，在缺乏人类指令数据的任务上也表现很好；



### 能力
- In-context learning
- Instruction following
- Step-by-step reasoning

### 关键技术
- Scaling: 更多的模型参数、数据量和训练计算
- Training: 分布式训练策略，提高训练稳定性
- Ability eliciting: 能力引导。设计合适的任务指令或具体的上下文学习策略。以在庞大的语料库中学习。
- Alignment tunning: 利用RLHF(reinforcement learning with human feedback) 实现微调，避免输出一些不安全或者不符合人类正向价值观的回复。
- Tools manipulation: 工具操作。让模型能使用搜索引擎，计算器或者给模型安装插件等工具。

## 各种名词解释与由来
**Prompt**
user prompt
Agent Tools
Fcuntion Calling
System Prompt
AI Agent
MCP

system prompt -> function calling


## 参考文章
[万字长文入门大语言模型（LLM）](https://zhuanlan.zhihu.com/p/654041855)

