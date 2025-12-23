# Everything I know about good API design

## Designing APIs is a balance between familiarity and flexibility

好的API应该是 boring 的，熟悉的，让人一看就知道是开什么的，而不需要额外花时间去思考如何使用他。

API一旦设计出来并使用是很难更改的，这就需要API的构建者在一开始就把API的设计做好。这需要尽可能简单的API，但是往往构建者希望API能保持长期的灵活性，因此广义上讲API就是在这两个不相容的目标之间找到平衡。

## WE DO NOT BREAK USERSPACE
你永远不应该仅仅因为它更整洁，或者因为它有点尴尬而对 API 进行更改。HTTP 规范中的“referer”标头是著名的“referrer”一词的拼写错误，但他们没有更改它， 因为我们不会破坏用户空间 。

## Changing APIs without breaking userspace

The answer is versioning.
即版本控制

版本控制通常是最终手段，在此之前我们可以做一些翻译层来继续使用旧的API。

## The success of your API depends entirely on the product

产品够好，需要去使用，再烂的 api 也得去看。

两款相当的产品，API的优秀设计才能体现出来。

## Poorly-designed products will usually have bad APIs



## 参考
[Everything I know about good API design](https://www.seangoedecke.com/good-api-design/)  