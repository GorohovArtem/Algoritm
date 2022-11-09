> Veronika Makarova:
# Алгоритм проходится по циклу пока искомое число не будет равно 1, проверяя при этом его на чётность/нечётность, считает количество матчей, которое необходимо сыграть до того момента пока количество участников не будет равно 1
# Сложность - приблизительно O(log(n))


class Solution:
    def numberOfMatches(self, n: int) -> int:
        count = 0                     # счётчик = 0, т.е. кол-во матчей равно нулю
        while n != 1:                 # пока команд больше 1 (если команда всего одна, то нужно 0 матчей, вернется 0 сразу)
            if n % 2 == 0:            # если четное количество команд
                count += n / 2        # то матчей нужно ровно половина от всех команд (играют n/2 против n/2)
                n = n / 2             # теперь n = половина от изначального кол-ва команд
            else:                     # если команд нечетное кол-во
                count += (n - 1) / 2  # то нужно сыграть половине команд с другой половиной (за вычетом одной, которая автоматом в след. этап), т.е. вычитаем 1 команду и делим нацело на 2
                n = (n - 1) / 2 + 1   # теперь n стало 'деление нацело всех изначальных команд на 2' + 1 команда
        return int(count)             # возвращаем кол-во матчей

> Veronika Makarova:
# Алгоритм проходит по циклу len(stones) количество раз. Если в jewels есть элемент stones, то count увеличивается на 1
# Сложность - O(n+m)


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        counter = 0               # счетчик = 0
        for i in stones:          # зашла в камни
            if i in jewels:       # прохожу по каждому драгоценному (не перейду в следующий обычный камень, пока не 'переберу' все драгоценные), если есть совпадение
                counter += 1      # инкрементирую счетчик
        return counter            # возвращаю счетчик
