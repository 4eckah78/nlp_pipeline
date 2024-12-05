import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nlp = spacy.load("ru_core_news_sm")

DOCS = [
    "Купил телефон, очень доволен, работает отлично",
    "Ноутбук не оправдал ожиданий, батарея быстро садится",
    "Заказал наушники, доставка быстрая, качество супер!",
    "Проблема с гарантией, отказываются менять товар",
    "Отличный телевизор, яркий экран, удобное меню",
]

vectorizer = TfidfVectorizer()
tf_idf_matrix = vectorizer.fit_transform(DOCS)


def get_tokens(text: str) -> list:
    doc = nlp(text)
    tokens = [
        token.lemma_.lower()
        for token in doc
        if not token.is_stop and not token.is_punct and not token.is_space
    ]
    return tokens


def search_top_3(query: str) -> list:
    processed_query = get_tokens(query)
    to_tranform = " ".join(processed_query)
    query_vector = vectorizer.transform([to_tranform])
    similarities = cosine_similarity(query_vector, tf_idf_matrix).flatten()
    top_indices = similarities.argsort()[-3:][::-1]
    return [DOCS[i] for i in top_indices]
