s1 = {'Рентген','Лоренц','Зееман','Кюри','Милликен', 'Сигбан', 'Франк', 'Герц'}
s2 = {'Фишер','Резерфорд','Кюри','Прегль'}
answer = []
for el1 in s1:
    for el2 in s2:
        if el1 == el2:
            answer.append(el1)

print(answer)