import time
import random
def _maopao_sort_(list):
    for i in range(len(list)):
        j=i+1
       
        for j in range(i+1,len(list)):
            if list[i] > list[j]:
                
                temp=list[j]
                list[j]=list[i]
                list[i]=temp
               
    result='排序结果'+','.join(map(str,list))
    
def random_int_list(start, stop, length):
    start, stop = (int(start), int(stop)) if start <= stop else (int(stop), int(start))
    length = int(abs(length)) if length else 0
    random_list = []
    for i in range(length):
        random_list.append(random.randint(start, stop))
    return random_list

if __name__=="__main__":
    #生成随机数组
    #生成10000个随机数
    array1=random_int_list(0,1000000,10000)
    t1 = time.time()

    _maopao_sort_(array1)
    t2=time.time()
    print(t2-t1)