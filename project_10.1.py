import pandas as pd
import random
# Исходные данные
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Создание словаря для one-hot кодирования
categories = sorted(set(data['whoAmI']))
categories_dict = {category: [1 if value == category else 0 for value in categories] for category in categories}

# Преобразование столбца в one-hot формат
one_hot_data = pd.DataFrame([categories_dict[value] for value in data['whoAmI']], columns=categories)

# Объединение с исходным DataFrame
data = pd.concat([data, one_hot_data], axis=1)

# Вывод результатов
print(data.head())
