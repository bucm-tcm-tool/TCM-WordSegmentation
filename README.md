# TCM-WordSegmentation
## What is it?
This is an automatic word segmentation model of electronic text in traditional Chinese medicine (TCM) based on SentencePiece, which can better achieve the segmentation of professional terms such as Chinese medicine symptoms, Chinese medicine and prescriptions. 

这是一个基于SentencePiece训练的中医电子文本自动分词模型，可以较好地实现中医症状、中药、方剂等专业术语的切分。

## What can be used for?
You can use it for word segmentation of electronic texts in TCM.

你可以将它用于中医电子文本的分词。

## How to use it?
Reference the example.py
参考example.py

## Results
 ### Example
 Input：使用中医经典方剂桂枝汤治疗营卫不和。

 ### Jieba
 Output : 使用 中医 经典 方剂 桂枝汤 治疗 营卫 不 和 。
 ### LTP
 Output : 使用  中医  经典  方剂  桂枝汤  治疗  营  卫  不和  。

 ### TCM-WordSegmentation
 Output : 使用 中医  经典方剂  桂枝汤 治疗 营卫不和 。

## cite info:
Liu S, Zhou L, Li C, et al. Research on Modeling of Traditional Chinese Medicine Word Segmentation Model Based on SentencePiece[J/OL].World Chinese Medicine:1-6[2021-05-09].http://kns.cnki.net/kcms/detail/11.5529.R.20210429.1546.048.html.
