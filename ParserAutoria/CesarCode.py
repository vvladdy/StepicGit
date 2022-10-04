# sortSequence([3,2,1,0,5,6,4,0,1,5,3,0,4,2,8,0]) should return
# [1,2,3,0,1,3,5,0,2,4,8,0,4,5,6,0]

def sort_sequence(l):
    t=[]
    p=0
    for i in range(len(l)):
        if l[i]==0:
            t.append(sorted(l[p:i])+[0])
            p=i+1
    return [v for l in sorted(t,key=sum) for v in l]


lis = [3,2,1,0,5,6,4,0,1,5,3,0,4,2,8,0]
print(sort_sequence(lis))


# Пузырьковая сортировка
# Сравниваются два єлемента, начиная с начала, меньший перемещается на раннюю
# позицию, а больший сравнивается дальше

def bubbleSort(alist):
    for passnum in range(len(alist)-1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

alist = [54,26,93,17,77,31,44,55,20]
bubbleSort(alist)
print(alist)

# Пузырьковая сортировка
# Сравниваются два єлемента, начиная с начала, меньший перемещается на раннюю
# позицию, а больший сравнивается дальше. Если первый эл-нт меньше второго,
# то расчеты прекращаются, берутся следующие элементы до очередного False

def shortBubbleSort(alist):
    exchanges = True
    passnum = len(alist)-1
    while passnum > 0 and exchanges:
       exchanges = False
       for i in range(passnum):
           if alist[i]>alist[i+1]:
               exchanges = True
               temp = alist[i]
               alist[i] = alist[i+1]
               alist[i+1] = temp
       passnum = passnum-1

alist=[20,30,40,90,50,60,70,80,100,110]
shortBubbleSort(alist)
print(alist)

# Сортировка выбором
# Сравниваются два єлемента, начиная с начала. Больший элемент перемещается в
# конец списка, а меньший остается на своем месте. и так до конца.

def selectionSort(alist):
   for fillslot in range(len(alist)-1,0,-1):
       positionOfMax=0
       for location in range(1,fillslot+1):
           if alist[location]>alist[positionOfMax]:
               positionOfMax = location

       temp = alist[fillslot]
       alist[fillslot] = alist[positionOfMax]
       alist[positionOfMax] = temp

alist = [54,26,93,17,77,31,44,55,20]
selectionSort(alist)
print(alist)

# Сортировка методом вставки
# Находим меньший элемент и сравниваем его с предыдущими элементами. Если он
# больше какого-то. то вставляем его после меньшего.

def insertionSort(alist):
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue

alist = [54,26,93,17,77,31,44,55,20]
insertionSort(alist)
print(alist)

# Метод сортировки оболочкой. Список разбивается на несколько списков,
# с элементами выбранными в некоторой последовательности. Затем в них
# сортируются элементы. После чеого сортируются списки

def shellSort(alist):
    sublistcount = len(alist)//2
    while sublistcount > 0:

      for startposition in range(sublistcount):
        gapInsertionSort(alist,startposition,sublistcount)

      print("After increments of size",sublistcount,
                                   "The list is",alist)

      sublistcount = sublistcount // 2

def gapInsertionSort(alist,start,gap):
    for i in range(start+gap,len(alist),gap):

        currentvalue = alist[i]
        position = i

        while position>=gap and alist[position-gap]>currentvalue:
            alist[position]=alist[position-gap]
            position = position-gap

        alist[position]=currentvalue

alist = [54,26,93,17,77,31,44,55,20]
shellSort(alist)
print(alist)

# Метод деления списка пополам
# Сортировка слиянием — это рекурсивный алгоритм, который постоянно делит
# список пополам. Если список пуст или содержит один элемент, он сортируется
# по определению (базовый случай). Если список содержит более одного
# элемента, мы разделяем список и рекурсивно вызываем сортировку слиянием
# для обеих половин. Как только две половины отсортированы, выполняется
# основная операция, называемая слиянием. Слияние — это процесс объединения
# двух меньших отсортированных списков в один отсортированный новый список

def mergeSort(alist):
    #print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    #print("Merging ",alist)

alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print(alist)

# Быстрая сортировка

# Быстрая сортировка сначала выбирает значение, которое называется опорным
# значением. Несмотря на то, что существует множество различных способов
# выбора опорного значения, мы просто будем использовать первый элемент в
# списке. Роль опорного значения состоит в том, чтобы помочь разделить
# список. Фактическая позиция, которой принадлежит опорное значение в
# окончательном отсортированном списке, обычно называемая точкой разделения,
# будет использоваться для разделения списка для следующих вызовов сортировки.

def quickSort(alist):
   quickSortHelper(alist, 0, len(alist)-1)

def quickSortHelper(alist,first, last):
   if first < last:

       splitpoint = partition(alist, first, last)

       quickSortHelper(alist, first, splitpoint-1)
       quickSortHelper(alist, splitpoint+1, last)


def partition(alist, first, last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark

alist = [54,26,93,17,77,31,44,55,20]
quickSort(alist)
print(alist)

# БИНАРНЫЙ ПОИСК
def binary_search_iterative(array, element):
    mid = 0
    start = 0
    end = len(array)
    step = 0

    while (start <= end):
        print("Subarray in step {}: {}".format(step, str(array[start:end+1])))
        step = step+1
        print('Start:{}  End: {}  '.format(start, end))
        mid = (start + end) // 2
        print('Mid:{}'.format(mid))

        if element == array[mid]:
            return mid

        if element < array[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1

array = [1, 2, 5, 7, 13, 15, 16, 18, 24, 28, 29]
print('Index interactive method', binary_search_iterative(array, 28))

# БИНАРНЫЙ ПОИСК С ПОМОЩЬЮ РЕКУРСИИ
def binary_search_recursive(array, element, start, end):
    if start > end:
        return -1

    mid = (start + end) // 2
    if element == array[mid]:
        return mid

    if element < array[mid]:
        return binary_search_recursive(array, element, start, mid-1)
    else:
        return binary_search_recursive(array, element, mid+1, end)

array = [1, 2, 5, 7, 13, 15, 16, 18, 24, 28, 29]
print('Index recusive method ', binary_search_recursive(array, 28, 0,
                                                        len(array)))
