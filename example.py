import sentencepiece as spm # version == 0.1.91
import os

# model path
model_file = './tcm_model.model'

# sentencePiece 
sp = spm.SentencePieceProcessor()
sp.Load(model_file)

# example
example = sp.EncodeAsPieces('使用中医经方桂枝汤治疗营卫不和。')
print(example)
