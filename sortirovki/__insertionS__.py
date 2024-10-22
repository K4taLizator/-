import random
import time


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def measure_time(sort_function, arr):
    start_time = time.perf_counter()  # Засекаем время до начала сортировки
    sort_function(arr)  # Вызываем сортировку
    end_time = time.perf_counter()  # Засекаем время после завершения сортировки
    return end_time - start_time  # Возвращаем затраченное время в секундах

for shaq in [0,2000,5000,8000,11000,13000,16000,18000,20000,23000,27000,32000]:
    for test in range (0, 10):
        # Пример использования
        #--------------------------------------------------------------------------------------
        #array = [random.randint(1, shaq) for _ in range(shaq)] #рандом
        # ----------------------------------------------------------------------
        #array = list(range(0, shaq)) #полностью отсортированный массив
        #----------------------------------------------------------------------
        array = list(range(0, shaq)) #(90/10)

        # Определяем количество элементов, которые нужно перемешать (10% от 5000 = 500)
        num_elements_to_shuffle = int(0.1 * len(array))

        # Выбираем случайные индексы для перемешивания
        indices_to_shuffle = random.sample(range(len(array)), num_elements_to_shuffle)

        # Перемешиваем выбранные элементы
        for i in indices_to_shuffle:
            # Меняем местами элемент с случайным элементом в массиве
            random_index = random.randint(0, len(array) - 1)
            array[i], array[random_index] = array[random_index], array[i]
        #--------------------------------------------------------------------------------------
        #array  = list(range(shaq,0,-1)) #обратная

        #print("Первоначальный массив:", array)
        print("кол-во элементов - ", shaq)
        # Измеряем время сортировки
        execution_time = measure_time(insertion_sort, array)

        print(f"Время сортировки: {execution_time:.6f} секунд")
        #print("Отсортированный массив:", array)
        print()
