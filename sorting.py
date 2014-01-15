def selection_sort(lst):
    for i in range(0, len(lst) - 1):
        min_index = i
        
        for j in range(i, len(lst)):
            if lst[j] < lst[min_index]: min_index = j
            
        _swap(lst, i, min_index)

def insertion_sort(lst):
    for i in range(1, len(lst)):
        
        if lst[i] < lst[i - 1]:
            val = lst[i]
            j = i
            
            while j > 0 and val < lst[j - 1]:
                lst[j] = lst[j - 1]
                j -= 1

            lst[j] = val

def bubble_sort(lst):
    for i in range(0, len(lst)):
        for j in range(len(lst) - 1, i, -1):
            if lst[j] < lst[j - 1]: _swap(lst, j, j - 1)

def merge_sort(lst):
    _m_sort(lst, 0, len(lst) - 1)

def _m_sort(lst, left, right):
    if left >= right: return
    
    # _m_sort(lst, middle, right) would not terminate if middle = (left + right) // 2
    middle = (left + right + 1) // 2
    
    _m_sort(lst, left, middle - 1)
    _m_sort(lst, middle, right) 
    _merge(lst, left, middle, right)

def _merge(lst, left, middle, right):
    if middle > right or left >= middle: return # only one sublist, these are assumed to be already sorted
    
    tmp = []
    tmp_length = (right - left) + 1
    lower_index = left
    higher_index = middle

    for i in range(0, tmp_length):
        
        if higher_index > right or (lower_index < middle and lst[lower_index] < lst[higher_index]):
            tmp.append(lst[lower_index])
            lower_index += 1            
        else:
            tmp.append(lst[higher_index])
            higher_index += 1

    for i in range(0, tmp_length):
        lst[left + i] = tmp[i]

def imerge_sort(lst):
    n = len(lst) - 1
    step = 2
    
    while step < n:
        left = 0
        
        while left < n:
            right = min(left + step - 1, n)
            middle = left + step // 2 # possible that middle > right -> only one sublist, _merge will do nothing
            _merge(lst, left, middle, right)
            left += step

        step += step
    _merge(lst, 0, step // 2, n)

def quick_sort(lst):
    _q_sort(lst, 0, len(lst) - 1)

def _q_sort(lst, left, right):
    if left >= right: return
    
    pivot_index = _partition(lst, left, right)
    _q_sort(lst, left, pivot_index - 1)
    _q_sort(lst, pivot_index + 1, right)

def _pick(lst, i, j, k):
    if lst[i] <= lst[j]:        
        if lst[j] <= lst[k]:
            return j
        else:
            return k
    else:
        if lst[i] <= lst[k]:
            return i
        else:
            return k

def _partition(lst, left, right):
    if (right - left) + 1 > 2:
        _swap(lst, _pick(lst, left, (left + right) // 2, right), right) # choose median of three 
    else:
        _swap(lst, (left + right) // 2, right) # choose middle as pivot and swap it to right

    pivot_val = lst[right]
    pivot_index = left # will hold pivot_index at the end

    for i in range(left, right):
        if lst[i] < pivot_val:
            _swap(lst, i, pivot_index)
            pivot_index += 1

    _swap(lst, pivot_index, right)
    return pivot_index

def _swap(lst, i, j):
    if i == j: return    
    lst[i], lst[j] = lst[j], lst[i]