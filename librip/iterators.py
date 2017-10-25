# Итератор для удаления дубликатов


class Unique(object):
    def __init__(self, items, **kwargs):
        # Нужно реализовать конструктор
        # В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
        # в зависимости от значения которого будут считаться одинаковые строки в разном регистре
        # Например: ignore_case = True, Aбв и АБВ разные строки
        #           ignore_case = False, Aбв и АБВ одинаковые строки, одна из них удалится
        # По-умолчанию ignore_case = False
        self.ignore_case = kwargs.get('ignore_case', False)

        self.items = self.__uniq_list(items)
        self.index = 0
        self.length = len(self.items)

    def __uniq_list(self, lst):
        cheker = {}
        result = []
        if self.ignore_case:
            for i in lst:
                if i.lower() not in cheker:
                    cheker[i.lower()] = 0
                    result.append(i)
        else:
            for i in lst:
                if i not in cheker:
                    cheker[i] = 0
                    result.append(i)

        return result

    def __next__(self):
        if self.index == self.length:
            raise StopIteration
        self.index += 1
        return self.items[self.index - 1]


    def __iter__(self):
        return self

