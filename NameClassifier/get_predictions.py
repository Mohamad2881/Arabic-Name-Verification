from tensorflow.keras.models import load_model
from keras_preprocessing.sequence import pad_sequences

import numpy as np
import pickle
import os
from Notebooks.preprocessing_utlis import normalize

from typing import Dict, List


class Model():
    def __init__(self) -> None:
        self.__storage_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'saved_model')
        self.__model_path = os.path.join(self.__storage_path, 'tria2.h5')
        print(self.__model_path)
        self.__tokenizer_path = os.path.join(self.__storage_path, 'tokenizer2.pickle')

        self.model = load_model(self.__model_path)
        
        with open(self.__tokenizer_path, 'rb') as handle:
            self.tok = pickle.load(handle)


    def classify(self, sentence:List[str]) -> List[Dict]:
        # class_names = ['سلبي' , 'إيجابي']
        class_names = ['Fake Name' , 'Valid Name']
        sentence_normalized = [normalize(sent) for sent in sentence]

        sequence = self.tok.texts_to_sequences(sentence_normalized)
        sequence = pad_sequences(sequence, maxlen=26, padding='post', truncating='post')
        
        preds = self.model.predict(sequence)
        response = []
        for idx, pred in enumerate(preds):
            row_pred = {}
            row_pred['Name'] = sentence[idx]
            row_pred['result'] = class_names[np.round(pred[0]).astype('int')]
            row_pred['score'] = float(pred[0])

            response.append(row_pred)
        
        return response

            # print(pred, np.round(pred[0]))
            # print(sentence[idx], ' >> ', class_names[np.round(pred[0]).astype('int')], pred)
        # print(class_names[np.round(pred).astype('int')], pred)


# tst_sent = ['باسمم وحةد السد','محمد سعيد خلية', 'باسم وحيد السيد']
# m = Model()
# print(m.classify(tst_sent))
# # print(classify(tst_sent))

