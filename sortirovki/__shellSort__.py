import random
import math
import time


def shell_sort(unsorted, steps):
    step = len(unsorted) // 2
    while step > 0:
        j = step
        while j < len(unsorted):
            i = j - step
            while i >= 0:
                if unsorted[i + step] > unsorted[i]:
                    break
                else:
                    unsorted[i + step], unsorted[i] = unsorted[i], unsorted[i + step]
                i -= step
            j += 1

        step //= 2
    return unsorted


def shell_sort_hib(unsorted, steps):
    k = math.log(len(unsorted) - 1, 2)
    step = 2 ** int(k) - 1
    while step > 0:
        j = step
        while j < len(unsorted):
            i = j - step
            while i >= 0:
                if unsorted[i + step] > unsorted[i]:
                    break
                else:
                    unsorted[i + step], unsorted[i] = unsorted[i], unsorted[i + step]
                i -= step
            j += 1
        step = (step + 1) // 2 - 1
    return unsorted


def shell_sort_pratt(unsorted, steps):
    step = max(i for i in steps if i < len(unsorted))
    ind = steps.index(step)
    while ind >= 0:
        j = step
        while j < len(unsorted):
            i = j - step
            while i >= 0:
                if unsorted[i + step] > unsorted[i]:
                    break
                else:
                    unsorted[i + step], unsorted[i] = unsorted[i], unsorted[i + step]
                i -= step
            j += 1
        ind -= 1
        step = steps[ind]
    return unsorted


def measure_time(sort_function, arr, steps):
    start_time = time.perf_counter()  # Засекаем время до начала сортировки
    sort_function(arr, steps)  # Вызываем сортировку
    end_time = time.perf_counter()  # Засекаем время после завершения сортировки
    return end_time - start_time  # Возвращаем затраченное время в секундах


steps = sorted([(2 ** i) * (3 ** j) for i in range(7) for j in range(7)])
for shaq in [100,50000, 100000,150000,200000,250000,300000,350000,400000,450000,500000,550000,600000,650000,700000,750000,800000,850000,900000,950000,1000000]:
    # for shaq in [0, 1, 5, 10]:
    print('КОЛ-ВО ЭЛЕМЕНТОВ - ', shaq)
    for test in range(0, 10):
        # Пример использования
        # --------------------------------------------------------------------------------------
        array = [random.randint(1, shaq) for _ in range(shaq)]  # рандом
        # ----------------------------------------------------------------------
        #array = list(range(0, shaq)) #полностью отсортированный массив
        # ----------------------------------------------------------------------
        # array = list(range(0, shaq)) #(90/10)
        #
        # # Определяем количество элементов, которые нужно перемешать (10% от 5000 = 500)
        # num_elements_to_shuffle = int(0.1 * len(array))
        #
        # # Выбираем случайные индексы для перемешивания
        # indices_to_shuffle = random.sample(range(len(array)), num_elements_to_shuffle)
        #
        # # Перемешиваем выбранные элементы
        # for i in indices_to_shuffle:
        #     # Меняем местами элемент с случайным элементом в массиве
        #     random_index = random.randint(0, len(array) - 1)
        #     array[i], array[random_index] = array[random_index], array[i]
        # --------------------------------------------------------------------------------------
        #array  = list(range(shaq,0,-1)) #обратная

        # print("Первоначальный массив:", array)
        #        print("кол-во элементов - ", shaq)
        # Измеряем время сортировки
        execution_time = measure_time(shell_sort, array, steps)
        print(f"{execution_time:.6f}")
        execution_time = measure_time(shell_sort_hib, array, steps)
        print(f"{execution_time:.6f}")
        execution_time = measure_time(shell_sort_pratt, array, steps)
        print(f"{execution_time:.6f}")
        # print("Отсортированный массив:", array)
    print()

