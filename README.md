# TCM-WordSegmentation
## What is it?
这是一个基于SentencePiece训练的中医电子文本自动分词模型，可以较好地实现中医症状、中药、方剂等专业术语的切分。

This is an automatic word segmentation model of electronic text in traditional Chinese medicine (TCM) based on SentencePiece, which can better achieve the segmentation of professional terms such as Chinese medicine symptoms, Chinese medicine and prescriptions. 

## What can be used for?
你可以将它用于中医电子文本的分词。

You can use it for word segmentation of electronic texts in TCM.

## How to use it and get it?
参考example.py，如果需要使用，请联系作者：liushuangqiaobucm@163.com

Reference the example.py

If need the trained model file(tcm_model.model in example.py), please contact the author: liushuangqiaobucm@163.com

## Results
### Example
 Input：使用中医经典方剂桂枝汤治疗营卫不和。
 
 Jieba output : 使用 中医 经典 方剂 桂枝汤 治疗 营卫 不 和 。
 
 LTP output   : 使用  中医  经典  方剂  桂枝汤  治疗  营  卫  不和  。

 Our output   : 使用 中医  经典方剂  桂枝汤 治疗 营卫不和 。

## Cite info:
刘双巧,周璐,李彩艳,等.基于SentencePiece的中医学分词模型建模研究[J/OL].世界中医药:1-6[2021-05-09].http://kns.cnki.net/kcms/detail/11.5529.R.20210429.1546.048.html.

Liu S, Zhou L, Li C, et al. Research on Modeling of Traditional Chinese Medicine Word Segmentation Model Based on SentencePiece[J/OL].World Chinese Medicine:1-6[2021-05-09].http://kns.cnki.net/kcms/detail/11.5529.R.20210429.1546.048.html.
