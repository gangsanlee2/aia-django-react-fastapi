import numpy as np
from keras.preprocessing.text import Tokenizer
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB


class ImdbService(object):
    def __init__(self):
        pass

class KoreanClassifyService(object):
    def __init__(self):
        pass

    def hook(self, test_str):
        ko_str = '이것은 한국어 문장입니다.'
        ja_str = 'これは日本語の文章です。'
        en_str = 'This is English Sentences.'
        x_train = [self.count_codePoint(ko_str),
                   self.count_codePoint(ja_str),
                   self.count_codePoint(en_str)]
        y_train = ['ko', 'ja', 'en']
        clf = GaussianNB()
        clf.fit(x_train, y_train)

        ko_test_str = '안녕하세요'
        ja_test_str = 'こんにちは'
        en_test_str = 'Hello'
        x_test = [self.count_codePoint(ko_test_str), self.count_codePoint(ja_test_str), self.count_codePoint(en_test_str)]
        y_test = ['ko', 'ja', 'en']

        y_pred = clf.predict(x_test)
        print(y_pred)
        print(f'정답률: {accuracy_score(y_test, y_pred)}')

        pred = clf.predict([self.count_codePoint(test_str)])
        return pred[0]

    @staticmethod
    def count_codePoint(str):
        counter = np.zeros(65535)   # Unicode 코드 포인트 저장 배열
        for i in range(len(str)):
            code_point = ord(str[i])
            if code_point > 65535:
                continue
            counter[code_point] += 1
        counter = counter / len(str)
        return counter

    # 추가 예제
    def homonym_classification(self):
        text = """경마장에 있는 말이 뛰고 있다\n
               그의 말이 법이다\n
               가는 말이 고와야 오는 말이 곱다\n"""
        tokenizer = Tokenizer()
        tokenizer.fit_on_texts([text])
        vocab_size = len(tokenizer.word_index) + 1
        # 케라스 토크나이저의 정수 인코딩은 인덱스가 1부터 시작하지만,
        # 케라스 원-핫 인코딩에서 배열의 인덱스가 0부터 시작하기 때문에
        # 배열의 크기를 실제 단어 집합의 크기보다 +1로 생성해야하므로 미리 +1 선언
        print(f"단어 집합의 크기 : {vocab_size}")
        print(f"word index : {tokenizer.word_index}")
        sequences = list()
        for line in text.split('\n'): # \n 을 기준으로 문장 토큰화
            encoded = tokenizer.texts_to_sequences([line])[0]
            for i in range(1, len(encoded)):
                sequence = encoded[:i +1]
                sequences.append(sequence)
        print(f'학습에 사용할 샘플의 갯수: {len(sequences)}')
        print(sequences)

if __name__ == '__main__':
    k = KoreanClassifyService()
    #k.homonym_classification()
    KoreanClassifyService().hook("경마장에 있는 말이 뛰고 있다")
