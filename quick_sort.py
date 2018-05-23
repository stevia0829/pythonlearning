import random
import time
quick_sort = lambda array: array if len(array) <= 1 else quick_sort([item for item in array[1:] if item <= array[0]]) + [array[0]] + quick_sort([item for item in array[1:] if item > array[0]])  


#生成随机数组
def random_int_list(start, stop, length):
    start, stop = (int(start), int(stop)) if start <= stop else (int(stop), int(start))
    length = int(abs(length)) if length else 0
    random_list = []
    for i in range(length):
        random_list.append(random.randint(start, stop))
    return random_list

#生成1000个随机数
if __name__=="__main__":

    #生成10000个随机数
    array1=random_int_list(0,1000000,100000)
    t1 = time.time()

    array2=quick_sort(array1)
    t2=time.time()
    print(t2-t1)