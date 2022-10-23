'''my_list =[1,2,3]
iterator = iter(my_list)
#print(iterator)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
for elem in iterator:
    print(elem)
for elem in iterator:
    print(elem)#elem-результат (в данном случает 1,2,3)'''

'''class Counter:
    def __init__(self,max_number):
        self.i=0
        self.max_number = max_number
    def __iter__(self):
        self.i =0
        return  self
    def __next__(self):
        self.i +=1
        if self.i > self.max_number:
            raise StopIteration
        return  self.i
count = Counter(8)
for elem in count:
    print(elem)'''
#генераторы
'''def raise_to_the_degrees(number,max_degree):
    i=0
    for _ in range(max_degree):
        yield number**1#yield- означает тоже что и return.**-это поднесение до степеня
        i+=1
res = raise_to_the_degrees(122345,500)
print(res)

for _ in res:
    print(_)
print("new execution")
for _ in res:
    print(_)
'''
def raise_to_the_degrees(number):
    i=0
    while True:
        result = number**i
        yield result
        if result> 100**20:
            return
        i+=1
res = raise_to_the_degrees(122345)
print(res)
for _ in res:
    print(_)
print("new execution")
for _ in res:
    print(_)
