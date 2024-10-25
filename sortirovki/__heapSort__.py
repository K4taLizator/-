import random
import time


def heapify(arr, n, i):
    largest = i  # Инициализируем корень как наибольший
    left = 2 * i + 1  # левый потомок
    right = 2 * i + 2  # правый потомок

    # Проверяем, является ли левый потомок больше корня
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Проверяем, является ли правый потомок больше текущего наибольшего
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Если наибольший не корень
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Меняем местами

        # Рекурсивно делаем кучу для затронутого поддерева
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Построение кучи (перегруппировка массива)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Один за другим извлекаем элементы из кучи
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Меняем местами
        heapify(arr, i, 0)

def measure_time(sort_function, arr):
    start_time = time.perf_counter()  # Засекаем время до начала сортировки
    sort_function(arr)  # Вызываем сортировку
    end_time = time.perf_counter()  # Засекаем время после завершения сортировки
    return end_time - start_time  # Возвращаем затраченное время в секундах

for shaq in [0,50000, 100000,150000,200000,250000,300000,350000,400000,450000,500000,550000,600000,650000,700000,750000,800000,850000,900000,950000,1000000]:
    # for shaq in [0, 1, 5, 10]:
    print('КОЛ-ВО ЭЛЕМЕНТОВ - ', shaq)
    for test in range(0, 10):
        # Пример использования
        # --------------------------------------------------------------------------------------
        array = [random.randint(1, shaq) for _ in range(shaq)] #рандом
        # ----------------------------------------------------------------------
        #array = list(range(0, shaq))  # полностью отсортированный массив
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
        execution_time = measure_time(heap_sort, array)

        print(f"{execution_time:.6f}")  # print(f"Время сортировки: {execution_time:.6f}")
        # print("Отсортированный массив:", array)
    print()