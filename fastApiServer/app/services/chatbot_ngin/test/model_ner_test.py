import os

from app.admin.path import dir_path
from app.services.chatbot_ngin.models.ner.NerModel import NerModel
from app.services.chatbot_ngin.utils.Preprocess import Preprocess

p = Preprocess(word2index_dic=os.path.join(dir_path('train_tools'), 'dict/chatbot_dict.bin'),
               userdic=os.path.join(dir_path('utils'), 'utils/user_dic.tsv'))


ner = NerModel(model_name=os.path.join(dir_path('models'), 'ner/ner_model.h5'), proprocess=p)
query = '오늘 오전 13시 2분에 탕수육 주문 하고 싶어요'
predicts = ner.predict(query)
tags = ner.predict_tags(query)
print(predicts)
print(tags)

