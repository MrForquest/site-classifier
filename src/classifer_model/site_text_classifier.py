import joblib
import pymystem3
import re
from string import punctuation

from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder


class SiteTextClassifier:
    def __init__(self, dir_model_path):
        self.tfidf_vec = joblib.load(dir_model_path + "tfidf_vec.joblib")
        self.label_enc = joblib.load(dir_model_path + "label_encoder.joblib")
        self.clf_model = joblib.load(dir_model_path + "log_reg_complex.joblib")
        self.mystem = pymystem3.mystem.Mystem()

    def predict(self, texts: list):
        preprocessed_texts = [self.preprocess_text(txt) for txt in texts]
        tfidf_matrix = self.tfidf_vec.transform(preprocessed_texts)
        preds = self.clf_model.predict(tfidf_matrix)
        labels_preds = self.label_enc.inverse_transform(preds)
        return labels_preds

    def preprocess_text(self, text):
        text = re.sub(r"ё", "е", text.lower())
        text = re.sub(r"[^а-я ]", " ", text)
        text = re.sub(r"\b(\w){,2}\b", " ", text).strip()
        text = re.sub(r"\s+", " ", text).strip()

        tokens = self.mystem.lemmatize(text.lower())
        new_tokens = list()
        for token in tokens:
            if token not in russian_stopwords and token != " ":
                new_tokens.append(token)
        text = " ".join(new_tokens)
        return text


russian_stopwords = [
    "и",
    "в",
    "во",
    "не",
    "что",
    "он",
    "на",
    "я",
    "с",
    "со",
    "как",
    "а",
    "то",
    "все",
    "она",
    "так",
    "его",
    "но",
    "да",
    "ты",
    "к",
    "у",
    "же",
    "вы",
    "за",
    "бы",
    "по",
    "только",
    "ее",
    "мне",
    "было",
    "вот",
    "от",
    "меня",
    "еще",
    "нет",
    "о",
    "из",
    "ему",
    "теперь",
    "когда",
    "даже",
    "ну",
    "вдруг",
    "ли",
    "если",
    "уже",
    "или",
    "ни",
    "быть",
    "был",
    "него",
    "до",
    "вас",
    "нибудь",
    "опять",
    "уж",
    "вам",
    "ведь",
    "там",
    "потом",
    "себя",
    "ничего",
    "ей",
    "может",
    "они",
    "тут",
    "где",
    "есть",
    "надо",
    "ней",
    "для",
    "мы",
    "тебя",
    "их",
    "чем",
    "была",
    "сам",
    "чтоб",
    "без",
    "будто",
    "чего",
    "раз",
    "тоже",
    "себе",
    "под",
    "будет",
    "ж",
    "тогда",
    "кто",
    "этот",
    "того",
    "потому",
    "этого",
    "какой",
    "совсем",
    "ним",
    "здесь",
    "этом",
    "один",
    "почти",
    "мой",
    "тем",
    "чтобы",
    "нее",
    "сейчас",
    "были",
    "куда",
    "зачем",
    "всех",
    "никогда",
    "можно",
    "при",
    "наконец",
    "два",
    "об",
    "другой",
    "хоть",
    "после",
    "над",
    "больше",
    "тот",
    "через",
    "эти",
    "нас",
    "про",
    "всего",
    "них",
    "какая",
    "много",
    "разве",
    "три",
    "эту",
    "моя",
    "впрочем",
    "хорошо",
    "свою",
    "этой",
    "перед",
    "иногда",
    "лучше",
    "чуть",
    "том",
    "нельзя",
    "такой",
    "им",
    "более",
    "всегда",
    "конечно",
    "всю",
    "между",
]


class SiteTextClassifier:
    def __init__(self, dir_model_path):
        pass

    def predict(self, texts: list):
        pass
        return labels_preds

    def preprocess_text(self, text):
        pass
        return new_text
