from random import randint
import random
import secrets
import time

#랜덤배열생성기

def mkarray(n):

    array = []
    rev_array = []
    # 천
    for j in range(0,10):
        first_ran, first_rev = [],[]
        for i in range(0, n):
            num = random.randrange(1, n+1)
            first_ran.append(num)
            first_rev.append(i + 1)

        first_rev.reverse()

        array.append(first_ran)
        rev_array.append(first_rev)

    return array,rev_array


#버블정렬


def BubbleSort(li):
    start = time.time()
    length = len(li) - 1
    for i in range(length):
        for j in range(length - i):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
    return time.time() - start



#선택정렬

def SelectionSort(li):
    ttime = time.time()
    for i in range(len(li)-1):
        min_idx = i
        for j in range(i+1, len(li)):
            if li[min_idx] > li[j]:
                min_idx = j
        if min_idx != i:
            li[i], li[min_idx] = li[min_idx], li[i]
    return time.time() - ttime



#삽입정렬

def insertionSort(x):
    ttime = time.time()
    for size in range(1, len(x)):
        val = x[size]
        i = size
        while i > 0 and x[i-1] > val:
            x[i] = x[i-1]
            i -= 1
        x[i] = val
    return time.time() - ttime

#합병정렬

def mergeSort(x):
    ttime = time.time()
    if len(x) > 1:
        mid = len(x)//2
        lx, rx = x[:mid], x[mid:]
        mergeSort(lx)
        mergeSort(rx)

        li, ri, i = 0, 0, 0
        while li < len(lx) and ri < len(rx):
            if lx[li] < rx[ri]:
                x[i] = lx[li]
                li += 1
            else:
                x[i] = rx[ri]
                ri += 1
            i += 1
        x[i:] = lx[li:] if li != len(lx) else rx[ri:]
    return time.time() - ttime


#퀵정렬1 - 마지막인덱스

def quickSort1(arr, p, r):
    ttime = time.time()
    if p<r:
        q = partition(arr,p,r)
        quickSort1(arr,p,q-1)
        quickSort1(arr,q+1,r)
    return time.time()-ttime

def partition(arr,p,r):
    tmp = 0
    ttmp = 0
    x = arr[r]
    i = p-1
    for j in range(p,r):
        if arr[j] <= x:
            i = i+1
            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp
    ttmp = arr[i+1]
    arr[i+1] = arr[r]
    arr[r] = ttmp
    return i+1


#퀵정렬2 - 중간인덱스

def quickSort2(arr, p, r):
    ttime = time.time()
    if p<r:
        q = partition(arr,p,r)
        quickSort2(arr,p,q-1)
        quickSort2(arr,q+1,r)
    return time.time()-ttime

def partition(arr,p,r):
    tmp = 0
    ttmp = 0
    x = arr[r]
    i = p-1
    for j in range(p,r):
        if arr[j] <= x:
            i = i+1
            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp
    ttmp = arr[i+1]
    arr[i+1] = arr[r]
    arr[r] = ttmp
    return i+1


#퀵정렬3 - 랜덤인덱스

def quickSort3(arr, p, r):
    ttime = time.time()
    if p<r:
        pivot = randint(p,r)
        temp = arr[r]
        arr[r] = arr[pivot]
        arr[pivot] = temp


        q = partition(arr,p,r)
        quickSort3(arr,p,q-1)
        quickSort3(arr,q+1,r)
    return time.time() - ttime

def partition(arr,p,r):
    pivot = randint(p,r)
    tmp = arr[r]
    arr[r] = arr[pivot]
    arr[pivot] = tmp
    i = p-1
    for j in range(p,r):
        if arr[j] <= arr[r]:
            i = i+1
            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp
    tmp = arr[i+1]
    arr[i+1] = arr[r]
    arr[r] = tmp
    return i+1


if __name__ == "__main__":

    A,R = mkarray(1000)
    AA,RR = mkarray(10000)
    AAA, RRR = mkarray(100000)

    #for i in A:
    #    print(i)
    #for i in R:
    #    print(i)

    #1000
    selection = 0
    bubble = 0
    quick_mid = 0
    quick_final = 0
    quick_ran = 0
    insertion = 0
    merge = 0
    for i in A:
        quick_mid += quickSort2(i,0,int(len(i)-1/2))
        quick_final += quickSort1(i,0,len(i)-1)
        quick_ran += quickSort3(i, 0, len(i) - 1)
        bubble += BubbleSort(i)
        selection += SelectionSort(i)
        insertion += insertionSort(i)
        merge += mergeSort(i)
    quick_mid/= 10
    quick_final/=10
    quick_ran/=10
    bubble/=10
    selection/=10
    insertion/=10
    merge/=10

    #reverse

    r_selection = 0
    r_bubble = 0
    r_quick_mid = 0
    r_quick_final = 0
    r_quick_ran = 0
    r_insertion = 0
    r_merge = 0
    for i in R:
        r_quick_mid += quickSort2(i,0,int(len(i)-1/2))
        r_quick_final += quickSort1(i, 0, len(i) - 1)
        r_quick_ran += quickSort3(i, 0, len(i) - 1)
        r_bubble += BubbleSort(i)
        r_selection += SelectionSort(i)
        r_insertion += insertionSort(i)
        r_merge += mergeSort(i)
    r_quick_mid/= 10
    r_quick_final/=10
    r_quick_ran/=10
    r_bubble/=10
    r_selection/=10
    r_insertion/=10
    r_merge/=10

    #10000

    a_selection = 0
    a_bubble = 0
    a_quick_mid = 0
    a_quick_final = 0
    a_quick_ran = 0
    a_insertion = 0
    a_merge =0
    for i in AA:
        a_quick_mid += quickSort2(i,0,int(len(i)-1/2))
        a_quick_final += quickSort1(i, 0, len(i) - 1 )
        a_quick_ran += quickSort3(i, 0, len(i) - 1)
        a_bubble += BubbleSort(i)
        a_selection += SelectionSort(i)
        a_insertion += insertionSort(i)
        a_merge += mergeSort(i)
    a_quick_mid/= 10
    a_quick_final/=10
    a_quick_ran/=10
    a_bubble/=10
    a_selection/=10
    a_insertion/=10
    a_merge /=10

    #reverse

    rr_selection = 0
    rr_bubble = 0
    rr_quick_mid = 0
    rr_quick_final = 0
    rr_quick_ran = 0
    rr_insertion = 0
    rr_merge = 0
    for i in RR:
        rr_quick_mid += quickSort2(i,0,int(len(i)-1/2))
        rr_quick_final += quickSort1(i, 0, len(i) - 1)
        rr_quick_ran += quickSort3(i, 0, len(i) - 1)
        rr_bubble += BubbleSort(i)
        rr_selection += SelectionSort(i)
        rr_insertion += insertionSort(i)
        rr_merge += mergeSort(i)
    rr_quick_mid/= 10
    rr_quick_final/=10
    rr_quick_ran/=10
    rr_bubble/=10
    rr_selection/=10
    rr_insertion/=10
    rr_merge/=10


    #100000

    aa_selection = 0
    aa_bubble = 0
    aa_quick_mid = 0
    aa_quick_final = 0
    aa_quick_ran = 0
    aa_insertion = 0
    aa_merge = 0
    for i in AAA:
       aa_quick_mid += quickSort2(i,0,int(len(i)-1/2))
       aa_quick_final += quickSort1(i, 0, len(i) - 1 )
       aa_quick_ran += quickSort3(i, 0, len(i) - 1)
       aa_bubble += BubbleSort(i)
       aa_selection += SelectionSort(i)
       aa_insertion += insertionSort(i)
       aa_merge += mergeSort(i)
    aa_quick_mid/= 10
    aa_quick_ran/=10
    aa_quick_final/=10
    aa_bubble/=10
    aa_selection/=10
    aa_insertion/=10
    aa_merge/=10

    #reverse

    rrr_selection = 0
    rrr_bubble = 0
    rrr_quick_mid = 0
    rrr_quick_final = 0
    rrr_quick_ran = 0
    rrr_insertion = 0
    rrr_merge = 0
    for i in RRR:
        rrr_quick_mid += quickSort2(i,0,int(len(i)-1/2))
        rrr_quick_final += quickSort1(i, 0, len(i) - 1)
        rrr_quick_ran += quickSort3(i, 0, len(i) - 1)
        rrr_bubble += BubbleSort(i)
        rrr_selection += SelectionSort(i)
        rrr_insertion += insertionSort(i)
        rrr_merge += mergeSort(i)
    rrr_quick_mid/= 10
    rrr_quick_final/=10
    rrr_quick_ran/=10
    rrr_selection/=10
    rrr_bubble/=10
    rrr_insertion/=10
    rrr_merge/=10


    print("==================================================================================================================================================================")
    print("=============","     Random1000     ","     Reverse1000     ","     Random10000     ","     Reverse10000     ","     Random100000     ","     Reverse100000   ")
    print("Bubble",              bubble,                r_bubble,              a_bubble,              rr_bubble,               aa_bubble,                rrr_bubble)
    print("Selection",           selection,             r_selection,             a_selection,       rr_selection,              aa_selection,            rrr_selection)
    print("Insertion",          insertion,              r_insertion,          a_insertion,           rr_insertion,            aa_insertion,              rrr_insertion)
    print("Merge",              merge,                  r_merge,               a_merge,               rr_merge,               aa_merge,                 rrr_merge)
    print("Quick1",             quick_final,          r_quick_final,          a_quick_final,          rr_quick_final,           aa_quick_final,         rrr_quick_final     )
    print("Quick2",              quick_mid,            r_quick_mid,            a_quick_mid,           rr_quick_mid,             aa_quick_mid,           rrr_quick_mid       )
    print("Quick3",              quick_ran,           r_quick_ran,            a_quick_ran,            rr_quick_ran,             aa_quick_ran,           rrr_quick_ran       )