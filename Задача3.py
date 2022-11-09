# Алгоритм проходит по циклу len(stones) количество раз. Если в jewels есть элемент stones, то count увеличивается на 1
# Сложность - O(n+m)


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        counter = 0               # счетчик = 0
        for i in stones:          # зашла в камни
            if i in jewels:       # прохожу по каждому драгоценному (не перейду в следующий обычный камень, пока не 'переберу' все драгоценные), если есть совпадение
                counter += 1      # инкрементирую счетчик
        return counter            # возвращаю счетчик