#!/usr/bin/env python3 # Указывает операционной системе использовать интерпретатор Python 3 для выполнения этого скрипта. | Specifies that the script should be run using Python 3 interpreter.

def is_continuous_sequence(seq): #Определяет функцию is_continuous_sequence, которая проверяет, является ли последовательность непрерывной. | Defines the function is_continuous_sequence, which checks if a sequence is continuous.
    if (
        not isinstance(seq, list)
        or len(seq) < 2
        or not all(isinstance(x, int) and not isinstance(x, bool) for x in seq)
    ):
        return False # Проверяет, является ли переданный аргумент seq списком, имеет ли он длину больше 1 и состоит ли он только из целых чисел (не булевых). | Checks if seq is a list, has a length greater than 1, and contains only integers (not booleans).

    sorted_seq = sorted(seq) # Сортирует последовательность в порядке возрастания. | Sorts the sequence in ascending order.
    for i in range(1, len(sorted_seq)): #Перебирает элементы отсортированной последовательности, начиная с индекса 1. | Iterates over the elements of the sorted sequence, starting from index 1.
        if sorted_seq[i] - sorted_seq[i - 1] != 1:
            return False #Если разница между текущим элементом и предыдущим не равна 1, последовательность не непрерывна. | If the difference between the current element and the previous one is not 1, the sequence is not continuous.
    return True # Если все элементы последовательности были проверены и не было пропусков, возвращает True. | If all elements of the sequence have been checked and there are no gaps, returns True.

def main(): # Определяет функцию main, которая используется для запуска программы. | Defines the main function, which is used to run the program.
    print(is_continuous_sequence([4, 5, 6, 7]))     # Проверяет, является ли последовательность [4, 5, 6, 7] непрерывной и выводит результат True. | Checks if the sequence [4, 5, 6, 7] is continuous and prints the result True.
    print(is_continuous_sequence([1, 2, 4]))        # Проверяет, является ли последовательность [1, 2, 4] непрерывной и выводит результат False. | Checks if the sequence [1, 2, 4] is continuous and prints the result False.
    print(is_continuous_sequence(["a", "b", "c"]))  # Проверяет, является ли последовательность ["a", "b", "c"] непрерывной и выводит результат False, так как последовательность состоит не из чисел. | Checks if the sequence ["a", "b", "c"] is continuous and prints the result False, as the sequence consists of non-numeric values.

if __name__ == "__main__": 
    main() # Если скрипт выполняется напрямую (не импортируется как модуль), вызывает функцию main для запуска программы. | If the script is run directly (not imported as a module), calls the main function to execute the program.
