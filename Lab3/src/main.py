import spacy
from spacy.matcher import Matcher

# Загрузка модели
nlp = spacy.load("ru_core_news_lg")

# Пример текста для анализа
text = "Вчера я купил кофе за 100 рублей, а сегодня заплатил 1500 руб. за билеты в кино."

# Инициализация матчера
matcher = Matcher(nlp.vocab)

# Определение шаблона для денежных сумм
pattern = [{"LIKE_NUM": True}, {"ORTH": {"IN": ["рублей", "руб", "руб."]}}]

# Добавление шаблона в матчер
matcher.add("MONEY_PATTERN", [pattern])

# Обработка текста с помощью spaCy
doc = nlp(text)

# Извлечение денежных сумм
money_amounts = []
matches = matcher(doc)
for match_id, start, end in matches:
    money_amounts.append(doc[start:end].text)

# Вывод результатов
if money_amounts:
    print("Извлеченные денежные суммы:")
    for amount in money_amounts:
        print(amount)
else:
    print("Денежные суммы не найдены.")
