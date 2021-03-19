import random

words1 = ["Коллеги, ", "В то же время, ", "Однако, ", "Тем не менее, ", "Следовательно, ", "Соответственно, ", "Вместе с тем, ", "С другой стороны, "]
words2 = ["парадигма цифровой экономики ", "контекст цифровой трансформации ", "диджитализация бизнес-процессов  ", "прагматичный подход к цифровым платформам ", "совокупность сквозных технологий ", "программа прорывных исследований ", "ускорение блокчейн-транзакций ", "экспоненциальный рост Big Data "]
words3 = ["открывает новые возможности для ", "выдвигает новые требования ", "несёт в себе риски ", "расширяет горизонты ", "заставляет искать варианты ", "не оставляет шанса для ", "повышает вероятность ", "обостряет проблему "]
words4 = ["дальнейшего углубления ", "бюджетного финансирования ", "синергетического эффекта ", "компрометации конфиденциальных ", "универсальной коммодитизации ", "несанкционированной кастомизации ", "нормативного регулирования ", "практического применения "]
words5 = ["знаний и компетенций.", "непроверенных гипотез.", "волатильных активов.", "опасных экспериментов.", "государственно-частных партнёрств.", "цифровых следов граждан.", "нежелательных последствий.", "внезапных открытий."]

# Первое предложение точно должно начинаться с приветствия
curr = 0
# Генерация трёх абзацев для отчёта (как в примере)
for i in range(3):
    for j in range(3):
        # Вывод сгенерированной строки
        print(words1[curr] + words2[random.randint(0, 7)] + words3[random.randint(0, 7)] + words4[random.randint(0, 7)] + words5[random.randint(0, 7)])
        # Выбор начала следующего предложения, но так чтобы его начало не совпадало с началом предыдущего
        next = random.randint(0, 7)
        while curr == next:
            next = random.randint(0, 7)
        # Запоминаем с какого вводного слова началось предыдущее предложение
        curr = next
    # Переход на слудющий абзац
    print('')