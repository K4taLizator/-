import random
import time

def divide_and_conquer(arr, start, end):
    pivot_value = arr[(start + end) // 2]
    left = start - 1
    right = end + 1
    while True:
        left += 1
        while arr[left] < pivot_value:
            left += 1
        right -= 1
        while arr[right] > pivot_value:
            right -= 1
        if left >= right:
            return right
        arr[left], arr[right] = arr[right], arr[left]

def quicksort(arr):
    def recursive_sort(sub_array, start, end):
        if start < end:
            partition_index = divide_and_conquer(sub_array, start, end)
            recursive_sort(sub_array, start, partition_index)
            recursive_sort(sub_array, partition_index + 1, end)

    recursive_sort(arr, 0, len(arr) - 1)


def measure_time(sort_function, arr):
    start_time = time.perf_counter()  # Засекаем время до начала сортировки
    sort_function(arr)  # Вызываем сортировку
    end_time = time.perf_counter()  # Засекаем время после завершения сортировки
    return end_time - start_time  # Возвращаем затраченное время в секундах

for shaq in [0,50000, 100000,150000,200000,300000,400000,500000,600000,700000,800000,900000,1000000,1200000,1300000,1500000,1700000,1900000,2000000, 2250000,2500000,2750000,3000000, 3250000,3500000,3750000,4000000]:
#for shaq in [0, 1, 5, 10]:
    print('КОЛ-ВО ЭЛЕМЕНТОВ - ', shaq)
    for test in range (0, 10):
        # Пример использования
        #--------------------------------------------------------------------------------------
        #array = [random.randint(1, shaq) for _ in range(shaq)] #рандом
        # ----------------------------------------------------------------------
        array = list(range(0, shaq)) #полностью отсортированный массив
        #----------------------------------------------------------------------
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
        #--------------------------------------------------------------------------------------
        #array  = list(range(shaq,0,-1)) #обратная

        #print("Первоначальный массив:", array)
#        print("кол-во элементов - ", shaq)
        # Измеряем время сортировки
        execution_time = measure_time(quicksort, array)

        print(f"{execution_time:.6f}") #print(f"Время сортировки: {execution_time:.6f}")
        #print("Отсортированный массив:", array)
    print()