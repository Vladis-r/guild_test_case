class MarkoPoloGen:
    """
    Класс для генерации Марко Поло
    """

    def generate_list(self, arr: list):
        """
        Генерация из списка чисел
        """
        res = self._check_data_list(arr)
        if res is True:
            return [self.generate_one(num) for num in arr]
        return res

    def generate_range(self, start: int, end: int):
        """
        Генерация от числа start, до числа end в пределах от 1 до 1000
        """
        res = self._check_data_range(start, end)
        if res is True:
            return [self.generate_one(num) for num in range(start, end + 1)]
        return res

    def generate_one(self, num: int):
        """
        Генерация по одному числу
        """
        res = self._check_data_one(num)
        if res is True:
            if num == 0:
                return 0
            elif num % 3 == 0 and num % 5 == 0:
                return 'МаркоПоло'
            elif num % 3 == 0:
                return 'Марко'
            elif num % 5 == 0:
                return 'Поло'
            else:
                return num
        return res

    def _check_data_range(self, start, end):
        """
        Проверки при генерации по ренджу
        """
        if isinstance(start, int) and isinstance(end, int):
            if 0 <= start <= 1000 and 0 <= end <= 1000:
                if start <= end:
                    res = True
                else:
                    res = "mp_start не может быть меньше, чем mp_end"
            else:
                res = "Числа должны быть в диапазоне от 0 до 1000"
        else:
            res = "Отправленные данные должны быть типа int"
        return res

    def _check_data_list(self, list_of_mp):
        """
        Проверки при генерации по списку
        """
        if isinstance(list_of_mp, list):
            for index, item in enumerate(list_of_mp):
                if item.isnumeric() and 0 <= int(item) <= 1000:
                    list_of_mp[index] = int(item)
                    res = True
                else:
                    return "Неверные данные в списке"
        else:
            res = "Должен быть передан список"
        return res

    def _check_data_one(self, number):
        """
        Проверки при генерации по числу
        """
        if 0 <= number <= 1000:
            return True
        return "Число должно быть от 0 до 1000"


gen_marko_polo = MarkoPoloGen()
