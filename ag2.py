# используем список для обработки массивов 0 индексовых чисел
# добавляем в список исходные значения, потом найдем общее максимальное значение
# сложность = 0
class Solution:
    def getMaximumGenerated(n):
        nums = list()                   # создаём список
        for i in range(n+1):            # смотрим все числа
            if i == 0:                  # если i 0
                nums.append(0)          # добавляем 0 в список
            elif i == 1:                # если i  1
                nums.append(1)          # добавлем 1 в список
            elif i % 2 == 0:            # остаток от деления i = 0
                nums.append(nums[i // 2])# добавляем в список i//2
            else:                       # в других случаях вернем макс. число которое есть в списке.
                nums.append(nums[i // 2] + nums[(i // 2) + 1])


        return max(nums)