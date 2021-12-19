#2. Написать два алгоритма нахождения i-го по счёту простого числа.

#    Без использования «Решета Эратосфена»;
#    Используя алгоритм «Решето Эратосфена»
import time
def get_func_time(func):
    def wrapper(arg):
        start_time = time.time_ns()
        result = func(arg)
        stop_time = time.time_ns()
        delta_time = stop_time - start_time
        #print(f"Время выполнения функции: {delta_time} ns")
        #print(f"Результат выполнения функции:\n {result}")
        return result, delta_time
    return wrapper

@get_func_time
def the_sieve_of_eratosthenes(n):
    nums = list(range(n+1))[2:]
    for i in range(2, n):
        for j in nums:
            if (i != j) and (j%i == 0):
                nums.remove(j)
    return(nums)

@get_func_time
def get_prime_nums(n):
    prime_nums = list()
    count = 0
    for i in range(2, n+1):
        for j in range(2, i):
            if i%j == 0:
                count += 1
        if count == 0:
            prime_nums.append(i)
        count = 0
    return prime_nums


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    prime_nums = the_sieve_of_eratosthenes(1000)
    print(f"Простые числа: {prime_nums[0]}\nВремя выполнения программы: {prime_nums[1]} ns")
    prime_nums = get_prime_nums(1000)
    print(f"Простые числа: {prime_nums[0]}\nВремя выполнения программы: {prime_nums[1]} ns")

# Сложность алгоритма Решето Эратосфена: О(n* log(log(n)))
# Cложность второго алгоритма О(n*log(n))
#     1(ns)АЭ        2(ns)
#   140037400       198935700
#   37835800        37835800
#   51272200        81191200
#   47860200        74230800
#   59132100        71176900